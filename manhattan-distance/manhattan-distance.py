import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    return np.sum(np.abs(x-y),dtype=np.float64)