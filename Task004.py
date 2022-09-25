# Реализуйте алгоритм перемешивания списка.
# Old method
# from random import randint
# n = int(input('Введите размер списка: '))
# a = []
# for i in range(n):
#     a.append(randint(1, 150))
# print(f'Первоначальный список {a}')
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(f'Отсортированный список методом пузырька {a}')

# New method
import random
lst = [random.randint(1, 10) for i in range(random.randint(3, 8))]
lst_new = random.sample(lst, len(lst))
print('Original list: ', lst, '\nShuffled list: ', lst_new)