def conditional_decorator(condition):
    def decorator(func):
        def wrapper_one(*args, **kwargs):
            print("Wrapper one is called")
            return func(*args, **kwargs)

        def wrapper_two(*args, **kwargs):
            print("Wrapper two is called")
            return func(*args, **kwargs)

        # 조건에 따라 다른 wrapper 함수를 반환
        if condition:
            return wrapper_one
        else:
            return wrapper_two
    return decorator


@conditional_decorator(True)  # 조건에 따라 wrapper_one이 반환
def greet(name):
    print(f"Hello, {name}!")


@conditional_decorator(False)  # 조건에 따라 wrapper_two가 반환
def farewell(name):
    print(f"Goodbye, {name}!")


greet("Alice")  # wrapper_one이 실행됨
farewell("Bob")  # wrapper_two가 실행됨


# def log_decorator(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == 'info':
#                 print(f"INFO: Calling {func.__name__}")
#             elif level == 'debug':
#                 print(f"DEBUG: Arguments were: {args}, {kwargs}")
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
#
# @log_decorator('info')
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# @log_decorator('debug')
# def add(a, b):
#     return a + b
#
#
# greet("Alice")  # INFO 레벨의 로그 출력
# add(3, 4)       # DEBUG 레벨의 로그 출력


# def decorator(func):
#     def pre_processing_wrapper(*args, **kwargs):
#         print("Pre-processing logic")
#         return func(*args, **kwargs)
#
#     def post_processing_wrapper(*args, **kwargs):
#         # result = func(*args, **kwargs)
#         print("Post-processing logic")
#         # return result
#
#     # 모든 동작을 하나의 wrapper로 결합해 반환할 수도 있음
#     def combined_wrapper(*args, **kwargs):
#         print("Before everything")
#         pre_processing_wrapper(*args, **kwargs)
#         post_processing_wrapper(*args, **kwargs)
#         print("After everything")
#
#     return combined_wrapper
#
#
# @decorator
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("Alice")

# def method_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling method {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# class MyClass:
#     @method_decorator
#     def my_method(self):
#         print("Method is running")
#
#
# obj = MyClass()
# obj.my_method()


# def count_calls_decorator(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"Call {wrapper.calls} of {func.__name__}")
#         return func(*args, **kwargs)
#     wrapper.calls = 0
#     return wrapper
#
#
# @count_calls_decorator
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("Alice")
# greet("Bob")


# import time
#
#
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         print(args)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper
#
#
# @timer_decorator
# def some_function():
#     time.sleep(2)
#     print("Function is running")
#     return 1
#
#
# print(some_function())



# 기본 구조
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         # 실행 전 동작
#         result = original_function(*args, **kwargs)
#         # 실행 후 동작
#         return result
#     return wrapper_function
#
