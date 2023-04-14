from multiprocessing import Pool
import numpy as np

def f(x):
  return x*x

if __name__ == '__main__':
  v= np.random.rand(1000,1000)
  with Pool(5) as p:
    print(p.map(f,v))
    