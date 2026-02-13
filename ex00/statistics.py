def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if not args or not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Args have to be digits only")
        nb_digits = len(args)
        list_methods = ["std, quartile, mean, median, var"]
        for key, value in kwargs.items():
            if value == "mean":
                mean = sum(args) / nb_digits
                print(f"mean : {mean}")
            elif value == "quartile":
                first_quar = nb_digits // 4
                last_quar = nb_digits // (3/4)
                print(f"quartile : [{args[first_quar]}, {args[last_quar]}]")
            elif value == "median":
                sort = sorted(args)
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

    except:
        
