memor = []
def remember_result(func):
    def wrapper(*args):
        ans = func(*args)
        global memor
        try:
            print(f"last call: {memor[0]}")
        except: print(f"last call: None")
        memor = []
        memor.append(ans)
        
    return wrapper

@remember_result
def sum_list(*args):
    if type(args[0]) == int:
        result = 0
    else: result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)