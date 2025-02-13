import numpy as np

class DataLoader:
    def __init__(self, arr_len, seed=None):
        self.arr_len = arr_len
        if seed is not None:
            np.random.seed(seed)
        
    def generate_data(self):
        return np.random.permutation(np.arange(1, self.arr_len + 1))