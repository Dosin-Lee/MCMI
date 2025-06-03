import numpy as np
from entropy import entropy


def joint_entropy(X: np.ndarray) -> float:
    """Compute joint entropy (in bits) of the columns of X."""
    X = np.asarray(X)
    if X.ndim == 1:
        X = X[:, np.newaxis]

    _, counts = np.unique(X, axis=0, return_counts=True)
    P = counts.astype(float) / counts.sum()
    return -np.sum(P * np.log2(P + 1e-12))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    a = rng.integers(0, 4, size=(1000, 2))
    print(joint_entropy(a))
