import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X)
    Xc = X - np.mean(X,axis=0,keepdims=True)
    C = np.dot(np.transpose(Xc),Xc)/(Xc.shape[0]-1)
    evals,evecs = np.linalg.eig(C)
    evals = evals.real
    idx = np.argsort(evals)[::-1]
    sorted_evals = evals[idx]
    sorted_evecs = evecs[:, idx]
    top_k_evals = sorted_evals[:k]
    top_k_evecs = sorted_evecs[:, :k]
    Xproj = Xc @ top_k_evecs
    return Xproj