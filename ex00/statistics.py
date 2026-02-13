def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if args:
            sort = sorted(args)
            nb_digits = len(args)
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Args have to be digits only")
        list_methods = ["std" , "quartile", "mean", "median", "var"]
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
                    median = (sort[nb_digits // 2 - 1] + sort[nb_digits // 2]) / 2
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

