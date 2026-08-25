import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x = np.asarray(a, dtype=np.float64)
    y = np.asarray(b, dtype=np.float64)
    
    nx = np.linalg.norm(x)
    ny = np.linalg.norm(y)
    
    if nx == 0 or ny == 0:
        return 0.0
    
    return float(np.dot(x, y) / (nx * ny))