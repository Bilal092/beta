import numpy as np
import scipy as sp
from scipy.linalg import sqrtm

def Bures_Distance(B, A):
    assert A.shape == B.shape, "Arrays must be of same shape."
    assert len(A.shape) == 2, "Input must 2-D."
    assert len(B.shape) == 2, "Input must 2-D."
    assert A.shape[0] == B.shape[0], "Input must be square."
    assert B.shape[0] == B.shape[0], "Input muyst be square."

    return np.sqrt(np.trace(A + B - 2*sp.linalg.sqrtm(B@A)))