def square(x: int | float) -> int | float:
    return x * x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = x
    def inner() -> int | float:
        nonlocal count
        # Permet de modifier la variable de la fonction outer
        # On applique la fonction passée en argument à 'count'
        count = function(count)
        return count
    return inner