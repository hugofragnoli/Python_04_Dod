def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if not args or not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Args have to be digits only")
        nb_digits = len(args)
        list_methods = ["std, quartile, mean, median, var"]
        sort = sorted(args)
        for key, value in kwargs.items():
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
            # elif value == "std":
            #     std = sum(args)
            # elif value == "var":
            #     var = 
            else:
                print("ERROR")
        return

    except Exception as e:
        print(f"Error : {e}")
        return None

