def callLimit(limit: int):
    count = 0  # a valider

    def callLimiter(function):

        def limit_function(*args: any, **kwargs: any):
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
