import numpy as np


def entropy(X: np.ndarray) -> np.ndarray:
    """Compute entropy (in bits) for each column of X."""
    X = np.asarray(X)
    if X.ndim == 1:
        X = X[:, np.newaxis]

    n, m = X.shape
    H = np.zeros(m)
    for col in range(m):
        column = X[:, col]
        values, counts = np.unique(column, return_counts=True)
        P = counts.astype(float) / counts.sum()
        H[col] = -np.sum(P * np.log2(P + 1e-12))
    return H


if __name__ == "__main__":
    # Simple test
    rng = np.random.default_rng(0)
    data = rng.integers(0, 4, size=(1000, 1))
    print(entropy(data))
