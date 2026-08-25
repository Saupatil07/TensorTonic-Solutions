import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    d = np.sqrt(np.sum(np.square(x-y),dtype=np.float64))
    return d