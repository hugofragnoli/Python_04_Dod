def callLimit(limit: int):
    """
    Un décorateur d'ordre supérieur qui restreint
    le nombre de fois
    qu'une fonction peut être exécutée.

    Args:
        limit (int): Le nombre maximum d'appels
        autorisés pour la fonction décorée.

    Returns:
        Callable: Un décorateur (callLimiter)
        configuré avec la limite spécifiée.
    """
    count = 0  # a valider

    def callLimiter(function):
        """
        Le décorateur effectif qui reçoit la fonction à protéger.

        Args:
            function (Callable): La fonction que l'on souhaite limiter.

        Returns:
            Callable: La version enveloppée (wrapper) de la fonction.
        """

        def limit_function(*args: any, **kwargs: any):
            """
            Le wrapper qui vérifie le compteur avant chaque exécution.

            Cette fonction utilise la variable 'count' définie dans la portée
            du parent pour suivre l'état entre plusieurs appels.

            Args:
                *args (any): Arguments positionnels passés à la fonction.
                **kwargs (any): Arguments nommés passés à la fonction.

            Returns:
                any: Résultat de l'incrémentation du compteur si l'appel est
                     autorisé, ou None si la limite est atteinte.
            """
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwargs)
            else:
                print(f"function {function} call too many times")
                return
            return count
        return limit_function
    return callLimiter
