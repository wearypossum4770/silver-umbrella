from functools import wraps


def fetch_addresses(func):
    """Grabs Avaialble Addresses"""

    @wraps(func)
    def inner_function(*args, **kwargs):
        """something"""

    return func(*args, **kwargs)
    return inner_function


def decorator(arg1, arg2):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f"Arguements passed to decorator {arg1} and {arg2}")
            function(*args, **kwargs)

        return wrapper

    return inner_function


@decorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)


print(print_args(1, 2, 3))


def decorator(arg1, arg2):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(dir(function))
            print(kwargs.request.user)
            Profile.objects.get()
            print(f"Arguements passed to decorator {arg1} and {arg2}")
            function(*args, **kwargs)

        return wrapper

    return inner_function
