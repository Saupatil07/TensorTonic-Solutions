import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    means = np.mean(X, axis=0, keepdims=True)
    deviations = X - means
    cov = (deviations.T @ deviations) / (X.shape[0] - 1)
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)

    return corr