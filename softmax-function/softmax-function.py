import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.atleast_1d(x)
    print(len(x))
    print(x.ndim)
    if x.ndim==1:
        numerator = np.exp(x-max(x))
        denominator = np.sum(numerator)
        return numerator/denominator
    else:
        soft_list = []
        for i in range(len(x)):
            numerator = np.exp(x[i]-max(x[i]))
            denominator = np.sum(numerator)
            soft_list.append(numerator/denominator)
        return np.array(soft_list)