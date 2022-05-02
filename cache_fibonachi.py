def cache(func):
    cache = {}

    def wrraped(*args, **kwargs):
        nonlocal cache
        if not cache.get(args):
            old_func = func(*args, **kwargs)
            cache[args] = old_func
            return old_func
        else:
            return cache[args]

    return wrraped


@cache
def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(int(input())))
