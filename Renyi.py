#%%

import numpy as np
import scipy as sp 

#%%
# Renyi Entropy function
'''
This script computes Renyi Entropy of a point on probaility Simplex.
'''

def Entropy(p, alph):
    assert(np.all(p >= 0)),"Probabilities cannot be negative"
    assert(alph >=0 ), "order cannot be nagative"
    # Shannon entropy
    if alpha == 1:
        return -sum(np.log2(p**p))
    # Min Entropy
    elif alpha == np.inf:
        return -np.log2(np.max(2))  
    else:
        return (1/(1-alph)) * np.log2(np.sum(p**alph))


# %%
