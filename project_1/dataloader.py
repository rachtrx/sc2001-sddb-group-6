import numpy as np

class DataLoader:
    def __init__(self, arr_len):
        self.arr_len = arr_len
        
    def generate_data(self):
        return np.random.permutation(np.arange(1, self.arr_len + 1))