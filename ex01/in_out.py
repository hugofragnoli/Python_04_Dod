def square(x: int | float) -> int | float:
    return x * x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    list_func = {
        "square": square,
        "pow": pow
    }
    if function not in list_func:
        print(f"Unknown function: {function} please pass 'square' or 'pow' as function")
        return 0
    
    res = list_func[function](x)
    return res