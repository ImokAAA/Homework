called_f = {}
def call_once(func):
    def wrapper(*args, **kwargs):
        global called_f
        print(func.__name__)
        if func.__name__ in called_f.keys():
            return called_f[func.__name__]
        else: 
            result = func(*args, **kwargs)
            called_f[func.__name__] = result
            return result
    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))
print(called_f.items())