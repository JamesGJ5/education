import numpy as np
from memory_profiler import profile

@profile
def example_one():
    d = np.ones([100, 1000, 1000])
    return d

if __name__=='__main__':
    example_one()