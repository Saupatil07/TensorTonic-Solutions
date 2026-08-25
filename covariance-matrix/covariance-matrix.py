import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    X_c = X - np.mean(X,axis=0)
    return (np.dot(np.transpose(X_c),X_c)) / (len(X) - 1)