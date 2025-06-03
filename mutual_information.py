import numpy as np
from entropy import entropy
from joint_entropy import joint_entropy


def mutual_information(X: np.ndarray, Y: np.ndarray) -> float:
    """Return the mutual information (in bits) of X and Y."""
    X = np.asarray(X)
    Y = np.asarray(Y)
    if X.ndim == 1:
        X = X[:, np.newaxis]
    if Y.ndim == 1:
        Y = Y[:, np.newaxis]
    if X.shape[0] != Y.shape[0]:
        raise ValueError("X and Y must have the same number of rows")

    return joint_entropy(X) + entropy(Y)[0] - joint_entropy(np.hstack([X, Y]))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    X = rng.integers(0, 4, size=(1000, 2))
    Y = rng.integers(0, 3, size=(1000, 1))
    print(mutual_information(X, Y))
