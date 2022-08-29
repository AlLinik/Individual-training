# def decorate(fn):
#     print('start')
#     fn()
#     print('stop')
#
# @decorate
# def function1():
#     print('1')
#
# @decorate
# def function2():
#     print('2')

# def my_shiny_new_decorator(function_to_decorate):
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate()
#         print("А я - код, срабатывающий после")
#
#     return the_wrapper_around_the_original_function
#
# def stand_alone_function():
#     print("Я простая одинокая функция")

# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()

# stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function()

# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Я простая одинокая функция")
# another_stand_alone_function()

# def decorate1(func):
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper

# def decorate2(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper

# def function(food="--ветчина--"):
#     print(food)
# function()

# function = decorate1(decorate2(function))
# function()

# @decorate1
# @decorate2
# def function(food="--ветчина--"):
#     print(food)
# function()

# @decorate2
# @decorate1
# def function(food="--ветчина--"):
#     print(food)
# function()

# def decorate(func):
#     def wrapper(arg1, arg2):
#         print("Аргументы:", arg1, arg2)
#         func(arg1, arg2)
#     return wrapper
#
# @decorate
# def full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
# full_name("Aliaksandr", "Linik")
def decoration_counter(fn):
    def wrapper():
        wrapper.count += 1
        return fn()

    wrapper.count = 0
    return wrapper

@decoration_counter
def function():
    print('Вызов function()')

function()
function()
function()

print('\nКоличество вызовов function() -', function.count)





