import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def cv10class(nexl: np.ndarray, indices: np.ndarray, param: dict) -> float:
    """10-fold cross validation classification."""
    M, N = nexl.shape
    results = []
    for i in range(1, 11):
        test = indices == i
        train = ~test
        train_data = nexl[train, :N-1]
        train_target = nexl[train, N-1]
        test_data = nexl[test, :N-1]
        test_target = nexl[test, N-1]

        if param.get("type") == 1:
            model = GaussianNB()
        elif param.get("type") == 2:
            model = svm.SVC(kernel="rbf", C=1, gamma=0.15)
        elif param.get("type") == 3:
            model = KNeighborsClassifier(n_neighbors=50)
        elif param.get("type") == 4:
            model = DecisionTreeClassifier()
        elif param.get("type") == 5:
            model = RandomForestClassifier(n_estimators=100)
        else:
            raise ValueError("Unsupported classifier type")

        model.fit(train_data, train_target)
        predict_label = model.predict(test_data)
        accuracy = np.mean(predict_label == test_target)
        results.append(accuracy)

    return float(np.mean(results))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    data = rng.integers(0, 5, size=(100, 6))
    indices = np.repeat(np.arange(1, 11), 10)
    print(cv10class(data, indices, {"type": 1}))
