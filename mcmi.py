"""Python implementation of the MCMI feature selection algorithm."""
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from mutual_information import mutual_information


def mcmi(X: np.ndarray, y: np.ndarray, max_features: int = 1000) -> np.ndarray:
    """Select features using Maximum Conditional Mutual Information (MCMI)."""
    X = np.asarray(X)
    y = np.asarray(y).ravel()

    X = np.nan_to_num(X)

    if not np.issubdtype(X.dtype, np.integer):
        disc = KBinsDiscretizer(n_bins=10, encode="ordinal", strategy="quantile")
        X = disc.fit_transform(X)

    newx = X
    EnY = mutual_information(y.reshape(-1, 1), y.reshape(-1, 1))  # not used but kept
    m, n = newx.shape

    MI = np.array([mutual_information(newx[:, [i]], y) for i in range(n)])
    ind = np.argsort(MI)[::-1]

    rem = ind[:max_features].tolist()
    opt = [rem.pop(0)]
    conf = newx[:, opt]
    mi_all = mutual_information(newx, y)

    while rem:
        mi_con = mutual_information(conf, y)
        con_mi = []
        for idx in rem:
            new_f = np.column_stack([conf, newx[:, idx]])
            mi_new = mutual_information(new_f, y)
            con_mi.append(mi_new - mi_con)
        con_mi = np.array(con_mi)
        order = np.argsort(con_mi)[::-1]
        if con_mi[order[0]] <= 0:
            break
        best_idx = rem[order[0]]
        opt.append(best_idx)
        conf = np.column_stack([conf, newx[:, best_idx]])
        rem.pop(order[0])
        zero_indices = np.where(con_mi == 0)[0]
        for z in sorted(zero_indices, reverse=True):
            if z < len(rem):
                rem.pop(z)
        if con_mi[order[0]] + mi_con >= mi_all:
            break

    for k in range(len(opt) - 1, -1, -1):
        con_new_f = np.delete(conf, k, axis=1)
        mi_con_new = mutual_information(con_new_f, y)
        if np.isclose(mi_con_new, mi_all):
            opt.pop(k)
            conf = con_new_f

    return np.array(opt)


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.integers(0, 5, size=(200, 10))
    y = rng.integers(0, 2, size=200)
    print(mcmi(X, y))
