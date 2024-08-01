# from  random import randit
# songs = ['pop-rock','rap','rock',
#          'cuntry','jazz','etno',
#          'fonk','pop','edm','indi','opera','hip-hop',
#          'trap','rnb','classic','shanson','bloos','punk-rock',
#          'electro','remix','mash up','covers']

# random_num = randit(0,23)
# print(songs[random_num])



# # декораторы 

# def my_decorator(func):
#     def wrapper():
#         print('before function call')
#         word = func()
#         print(word+'jhon')
#         print('after function call')
#     return wrapper    
 
# @my_decorator
# def say_hello():
    #   print = input('enter your name')
#     return 'hello'

# say_hello()   
# print(my_decorator(say_hello))

# @my_decorator
# def say_bye():
#     return 'bye'


# @property
# @classmethod
# @staticmethod



# декораторы с параметрами 

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('before function call')
#         func(*args, **kwargs)
#         print('after function call')
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print(f'hello{name}')

# say_hello('petya')

# @my_decorator
# def say_bye(name2,name3):
#     print(f'dye {name2} {name3}')

# say_bye('vasya',Name3='petya')



# def my_decorator1(func):
#     def wrapper():
#         print('function1 call')
#         func()
#     return wrapper



# def my_decorator2(func):
#     def wrapper():
#         print('function2 call')
#         func()
#     return wrapper

# @my_decorator1
# @my_decorator2
# def say_hello():
#     print('hello')

# say_hello()


# def repeat(num):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print("before")
#             for _ in range(num):
#                 result = func(*args,**kwargs)
#             return result  
#         return wrapper
#     return decorator

# @repeat(5)
# def say_hello(name):
#     print('hello' + name)

# say_hello('alice')    


# Напишите декоратор который  double_result который будет
# умножть на 2 результат функции

# Напшите декоратор который будет вызвать функцию с аргументами в
# обратном порядке
# подсказка [::-1]

# def num (a,b):
#     return a - b

# num(5,3)
# num(3,5)













