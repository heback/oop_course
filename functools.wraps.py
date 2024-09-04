import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper


@my_decorator
def say_hello():
    """This function says hello"""
    print("Hello!")


# 함수 이름과 docstring 확인
print(say_hello.__name__)
print(say_hello.__doc__)


