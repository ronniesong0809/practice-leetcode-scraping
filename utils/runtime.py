import time
import inspect

def runtime(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()

        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        print(f'{module.__name__:>18}/{func.__name__:<30} done in: {end - start:.2f} sec')
    return wrapper

def runtime_withoutFucName(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print(f'done in: {end - start:.2f} sec')
    return wrapper