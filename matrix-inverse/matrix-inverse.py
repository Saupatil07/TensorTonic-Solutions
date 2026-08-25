import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.asarray(A)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    n = A.shape[0]

    # [A | I]
    aug_mat = np.concatenate((A, np.eye(n)), axis=1)

    for i in range(n):
        # Find pivot row
        pivot_row = i + np.argmax(np.abs(aug_mat[i:, i]))

        # Singular matrix
        if np.isclose(aug_mat[pivot_row, i], 0):
            return None

        # Swap rows
        aug_mat[[i, pivot_row]] = aug_mat[[pivot_row, i]]

        # Normalize pivot row
        aug_mat[i] /= aug_mat[i, i]

        # Eliminate this column from all other rows
        for j in range(n):
            if j != i:
                aug_mat[j] -= aug_mat[j, i] * aug_mat[i]

    # Right half is A^-1
    return aug_mat[:, n:]
    