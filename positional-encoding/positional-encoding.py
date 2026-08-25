import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    position = np.arange(seq_len).reshape(-1, 1)
    freq = 1.0 / (base ** (np.arange(0, d_model, 2) / d_model))
    angles = position * freq

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])

    return pe