from scipy import io
import numpy as np


def load_matrix(filename):
    loadm = io.loadmat(filename)
    key_list = list(loadm.keys())
    matrix = loadm[key_list[3]]
    return np.array(matrix)


