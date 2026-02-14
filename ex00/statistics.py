def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calcule et affiche des statistiques de base sur une série de nombres.

    La fonction traite des arguments positionnels numériques et affiche les
    statistiques demandées via les arguments par mots-clés (kwargs).

    Args:
        *args (any): Une séquence de nombres (int ou float).
                     Doit être non vide pour effectuer les calculs.
        **kwargs (any): Les opérations demandées. Les valeurs autorisées sont :
                        'mean', 'median', 'quartile', 'std', 'var'.

    Comportement :
        - Si args vide, affiche "ERROR" pour chaque demande valide dans kwargs.
        - Si une valeur dans kwargs n'est pas dans la liste autorisée-> ignorée
        - Si un élément de args n'est pas un nombre, lève une ValueError.

    Statistiques calculées :
        - mean : La moyenne arithmétique.
        - median : La valeur centrale de la série triée.
        - quartile : Les 25e et 75e centiles (premier et troisième quartiles).
        - var : La variance (moyenne des carrés des écarts à la moyenne).
        - std : L'écart-type (racine carrée de la variance).
    """
    try:
        if args:
            sort = sorted(args)
            nb_digits = len(args)
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Args have to be digits only")
        list_methods = ["std", "quartile", "mean", "median", "var"]
        for key, value in kwargs.items():
            if value not in list_methods:
                continue

            if not args:
                print("ERROR")
                continue

            if value == "mean":
                mean = sum(args) / nb_digits
                print(f"mean : {mean}")
            elif value == "quartile":
                first_quar = sort[nb_digits // 4]
                last_quar = sort[(3 * nb_digits) // 4]
                print(f"quartile : [{first_quar}, {last_quar}]")
            elif value == "median":
                if nb_digits % 2 == 0:
                    median = (sort[nb_digits // 2 - 1] + sort[nb_digits //
                                                              2]) / 2
                else:
                    median = sort[nb_digits // 2]
                print(f"median : {median}")
            # std = ecart type = Racine de variance
            elif value == "std":
                mean_std = sum(args) / nb_digits
                sum_std = sum((x - mean_std) ** 2 for x in args)
                var_std = sum_std / nb_digits
                std = var_std ** 0.5
                print(f"std : {std}")
            # on a besoin de la variance donc on fera en dernier
            elif value == "var":
                mean_var = sum(args) / nb_digits
                sum_square = sum((x - mean_var) ** 2 for x in args)
                var = sum_square / nb_digits
                print(f"var : {var}")
            else:
                continue
        return

    except Exception as e:
        print(f"Error : {e}")
        return None
