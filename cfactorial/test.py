import time
import cfactorial




#   Timing decorator to measure the performance of each function
class TimerWrapper:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        s = time.time()
        self.f(*args, **kwargs)
        e = time.time()
        result = str(e - s)
        print(f'function:\n {self.f.__name__} took {result} seconds to run\n\n')




#   Main python factorial function
def python_factorial(n):
    if n < 1:
        return 1
    else:
        return n * python_factorial(n - 1)
    
    
    

SAMPLE_SIZE = 10000000
N_FACTORIAL = 20

@TimerWrapper
def py_test():
    for i in range(SAMPLE_SIZE):
        python_factorial(N_FACTORIAL)
        
        
@TimerWrapper
def C_test():
    for i in range(SAMPLE_SIZE):
        cfactorial.factorial(N_FACTORIAL)

        
        
        
if __name__ == '__main__':
    py_test()
    C_test()
    
