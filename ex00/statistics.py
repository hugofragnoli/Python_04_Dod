def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        if not args or not all(isinstance(x, (int, float)) for x in args):
            raise ValueError("Args have to be digits only")
        nb_digits = len(args)
        list_methods = ["std, quartile, mean, median, var"]
        for key, value in kwargs.items():
            if value in ["mean"]:
                mean = sum(args) / nb_digits
            elif value in "quartile":
                quartile = sum(args)
            elif value in "quartile":
                quartile = sum(args)
                
                
        

        print(list_args)
        print(list_kwargs)
        return

    except:
