import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.atleast_1d(x)
    print(x)
    if len(x) > 1:
        return np.maximum(x,0)
    else:
        return np.maximum(x,0)[0]