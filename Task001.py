# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Old method
# print('Введите число : ')
# n = int(input())
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# list = [factorial(i) for i in range(1, n + 1)]
# print(list)

# New method
from math import factorial
n = int(input('Введите число: '))
f = lambda x: 1 if x == 0 else x * factorial(x - 1)
lst = list(f(i) for i in range(1, n + 1))
print(lst)