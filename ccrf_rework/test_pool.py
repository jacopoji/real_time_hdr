from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support
import time

def func(a, b):
    print(a+b)
    return a + b

def main():
    a_args = [1,2,3]
    second_arg = 1
    init_time = time.time()
    
    with Pool() as pool:
        L = pool.starmap(func, [(1, 1), (2, 1), (3, 1)])
        #M = pool.starmap(func, zip(a_args, repeat(second_arg)))
        #N = pool.map(partial(func, b=second_arg), a_args)
        #assert L == M == N
    print("1",time.time()-init_time)
    
    init_time = time.time()
    time.clock()
    func(1,1)
    func(2,1)
    func(3,1)
    print("2",time.time()-init_time)
    print("2,clock",time.clock())


if __name__=="__main__":
    freeze_support()
    main()