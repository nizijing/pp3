def print_func_name(fn):
    def wrapper(*args, **kwargs):
        print("funcion: {}".format(fn.__name__))
        ret = fn(*args, **kwargs)
        return ret
    return wrapper

@print_func_name
def my_func():
    print("this is my function.")


# if use decorators
my_func()


# if not use decorators
f1 = print_func_name(my_func)
f1()
