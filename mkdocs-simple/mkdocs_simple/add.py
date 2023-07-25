import numpy as np

def add(x, y):
    ''' Add two numbers
    '''
    return x + y

def add_np(x, y):
    ''' Add two numbers with numpy silliness
    '''
    return np.array([x,y]).sum()