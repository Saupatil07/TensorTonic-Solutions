import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.asarray(matrix)
    eigen_val = np.sort(np.linalg.eigvals(matrix).real)
    return eigen_val