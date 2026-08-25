import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    m = np.asarray(matrix)
    if norm_type=='max':
        return m/np.max(m,axis=axis,keepdims=True)
    elif norm_type=='l1':
        return m/np.sum(m,axis=axis,keepdims=True)
    else:
        lengths = np.sqrt(np.sum(np.square(m), axis=axis, keepdims=True))
        result = np.divide(m, lengths, out=np.zeros_like(m).astype(float), where=lengths != 0)
        return result