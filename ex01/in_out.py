def square(x: int | float) -> int | float:
    x_square = x * x
    return x_square

def pow(x: int | float) -> int | float:
    x_pow = x ** x
    return x_pow

def outer(x: int | float, function) -> object:
    list_func = ["pow", "square"]
    if function not in list_func:
        print("Unknown function: please pass 'square' or 'pow' as function")
        return 0
    
    return