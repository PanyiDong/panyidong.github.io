---
title: "Intro To Numba/CuPy"
permalink: "/Parallel/NumbaCupy/"
mathjax: true
categories: media
layout: post
---

Introduction to Numba/CuPy to use GPU accelerate Python code.

#### Numba

Numba is a Just-in-Time (JIT) compiler which compiles Python bytecode from decorated function into machine code, and allows LLVM to inline functions, autovectorize loops and other optimization from C compiler.

1. jit

```python
import random
from numba import jit

@jit
def monte_carlo_pi(nsamples) :
    
    acc = 0
    for i in range(nsamples) :
        x = random.random()
        y = random.random()

        if (x ** 2 + y ** 2) < 1.0 :
            acc += 1
    
    return 4.0 * acc / nsamples
```

For above sample, where the goal is to calculate $\pi$ using Monte Carlo method, if there's no decoration of `@jit` and `nsamples` is a large number (usually for more accurate estimation and here partially for demonstration of improvement), the code can take sometime to run (Python is not very efficient in terms of `for` loops).  And with the decoration of `@jit`, the code can be compiled and run much faster.

However, one note here is that, for the first compiling, the runtime of the code may not seems favorable (compared to non decorated function), which is due to that the compiling using Numba can take sometime to finish. But the next time you run the code, you can see the drastic improvement in efficiency. (Run the code two times, see the difference.)

Some common compilation options for `jit`:

`nopython`: default set to `False`. During compilation, at default setting of `False`, when Numba faces codes that can not be compiled, the code then will run in Python style. (Take example of a function which returns a numerical/string mixed list, which can not be handled by machine code, if `nopython=False` set, the code will run in Python, no acceleration for the decoration.) However, if you are determined to accelerate the code efficiency, then you can set `nopython=True`, so that when compilation get issues, a error will prevent the code from running further.

`cache`: whether to store the compilation as cache, so next time of running will take advantages of the cache instead of compiling again.

`parallel`: whether to enable parallel compilation.

2. cuda.jit

To utilize the computation resources like GPU, `cuda.jit` is an option.

```python
import numpy as np
from time import perf_counter
from numba import cuda

@cuda.jit
def init_all(p_num, d_num, pos, accel, vel):
    for j in range(0, p_num[0]) :
        for i in range(0, d_num[0]) :
            pos[i,j] = 6.5
        # end for i
        for i in range(0, d_num[0]) :
            accel[i,j] = 4.2*pos[i,j]
        # end for i
    # end for j
    
    init_vel(p_num, d_num, pos, accel, vel)
# end def

@cuda.jit(device=True)
def init_vel(p_num, d_num, pos, accel, vel):
    for j in range(0, p_num[0]) :
        for i in range(0, d_num[0]) :
            vel[i,j] = pos[i,i] + accel[i,j] * 0.1*pos[i,j]
        # end for i
    # end for j
# end def

# main loop
d_num = np.zeros(1, dtype=int)
p_num = np.zeros(1, dtype=int)
d_num[0] = 5000
p_num[0] = 5000
pos = np.zeros(shape=(d_num[0], p_num[0]), dtype=np.float32)
accel = np.zeros(shape=(d_num[0], p_num[0]), dtype=np.float32)
vel = np.zeros(shape=(d_num[0], p_num[0]), dtype=np.float32)

start_time = perf_counter()
d_p_num = cuda.to_device(p_num)
d_d_num = cuda.to_device(d_num)
d_pos = cuda.to_device(pos)
d_accel = cuda.to_device(accel)
d_vel = cuda.to_device(vel)
init_all(p_num, d_num, pos, accel, vel)
stop_time = perf_counter()

print(pos)
print(vel)
print(accel)
print('')
print(' Elapsed wall clock time = %g seconds.' % (stop_time
start_time) )
print('')
```

For `cuda.jit`, use loops to work on non element by element operations.

Some common compilation options for `cuda.jit`:

`device`: set device to `True` so that different functions can be saved on same device to avoid multiple devices error.

3. vectorize

```python
import numpy as np
from time import perf_counter
from numba import vectorize

@vectorize(['float32(float32)'])
def set_pos(pos) :
    return 6.5
# end def

d_num = 5000
p_num = 5000
pos = np.zeros((d_num, p_num), dtype =np.float32)

start_time = perf_counter()
pos = set_pos(pos)
stop_time = perf_counter()

print(pos)
print('')
print(' Elapsed wall clock time = %g seconds.' % (stop_time - start_time))
print('')
```

`vectorize` is specifically designed to deal with element by element operations (on scalers), and can utilize advantages of both CPU and GPU.

Some common compilation options for `vectorize`:

`device`: set device to `cuda` to utilize GPU computation.

For further Numba supports, please visit [web](https://numba.readthedocs.io/en/stable/user/index.html) to review.

#### CuPy

CuPy is a NumPy-like API but with acceleration using GPU.

From NumPy:
```python
import numpy as np
x_cpu = np.array([1, 2, 3])
l2_cpu = np.linalg.norm(x_cpu)
```

Change it to GPU version:
```python
import cupy as cp
x_gpu = cp.array([1, 2, 3])
l2_gpu = cp.linalg.norm(x_gpu)
```

After above codes, `x_gpu` and `l2_gpu` are stored in GPU memory, if you wish it to be read by CPU instead, run `cp.asnumpy` or `cp.asarray` to convert them to NumPy CPU objects. However, one notice is that transferring data from GPU to CPU (using PCIE channel) and transferring back to GPU can take sometime (especially large datasets). If the data will later be accessed by GPU, try not to transfer it to CPU unless necessary.

CuPy can access CUDA base for data manipulation, supported features include (but not limited to) :

Linear Algebra functions: dot, matnul, linalg (SVD, eigh, trace, solve), transpose, etc.

Reduction along axes: sum, max, etc.

Mathematics functions: cos, ceil, log, etc.

Random functions: rand, random, etc.

Sort, Search, Count: sort, argmax, nonzero, etc.

Stats: mean, var, etc.

Sparse Matrix

FFT: Fourier Transformation. 

Other Nvidia libraries: cuFFT, cuBLAS, etc.

For further CuPy supports, visit [web](https://docs.cupy.dev/en/stable/reference/index.html) to review.