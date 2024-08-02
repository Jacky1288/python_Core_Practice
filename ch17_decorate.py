def func(message):
    def get_message(me):
        print("et_message is {}".format(me))

    return get_message(message)


# func("hello world")

# 函数的返回值也可以是函数

def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))

    return get_message


# send_message = func_closure()
# send_message('hello world')


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

# def greet():
#     print('hello world')
#
# greet = my_decorator(greet)
# greet()

@my_decorator
def greet():
    print('hello world')


greet()
