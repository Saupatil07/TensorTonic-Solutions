import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.array(x)
    leaky_list = []
    for i in range(len(x)):
        if x[i]<0:
            leaky_list.append(alpha*x[i])
        else:
            leaky_list.append(x[i])
    return np.array(leaky_list)
            