def square(x: int | float) -> int | float:
    """
    Calcule le carré d'un nombre.

    Args:
        x (int | float): Le nombre à élever au carré.

    Returns:
        int | float: Le résultat de x * x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calcule l'auto-puissance d'un nombre (x élevé à la puissance x).

    Args:
        x (int | float): La base et donc l'exposant.

    Returns:
        int | float: Le résultat de x**x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Crée une fermeture  qui applique de manière cumulative
    une fonction à une valeur initiale.

    Args:
        x (int | float): La valeur initiale de départ.
        function (callable): La fonction à appliquer (ex: square ou pow).

    Returns:
        function: La fonction interne 'inner' qui maintient l'état du calcul.
    """
    count = x

    def inner() -> int | float:
        """
        Applique la fonction stockée à la valeur courante et met à jour l'état

        Cette fonction utilise le mot-clé 'nonlocal' pour modifier la variable
        'count' définie dans l'espace de nom de la fonction 'outer'.

        Returns:
            int | float: La nouvelle valeur de 'count' après application
            de la fonction.
        """
        nonlocal count
        # Permet de modifier la variable de la fonction outer
        # On applique la fonction passée en argument à 'count'
        count = function(count)
        return count
    return inner
