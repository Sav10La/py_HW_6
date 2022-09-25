# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Old method
# lst = [1, 2, 3, 4, 5, 6]
# n = len(lst)
# def odd_sum(a, n):
#     odd = 0
#     for i in range(n):
#         if i % 2 == 1:
#             odd += a[i]
#     print("Сумма эелментов на нечетных позициях =", odd)
# print(lst)
# odd_sum(lst, n)

# New method
from random import randint
n = int(input('Введите размер списка: '))
lst = [int(randint(1, 10)) for i in range(n)]
print(f'Первоначальный список {lst}')
print(sum(lst[1::2]))