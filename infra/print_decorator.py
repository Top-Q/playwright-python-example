def step(func):
    def print_function(*args, **kwargs):
        func_name: str = func.__name__
        func_name = func_name.replace('_', ' ').capitalize()
        params: str = ""
        if kwargs:
            params = f"{kwargs}".replace("{", "").replace("}", "")
        if len(args) > 1:
            for i in range(1, len(args)):
                params = f"{params} '{args[i]}'"
        print(f"{func_name} {params}")
        return func(*args, **kwargs)
    return print_function





@step
def some_function(x, y):
    print(x + y)
    return x + y


if __name__ == '__main__':
    result = some_function(x=10, y=20)
    print(result)
