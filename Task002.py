# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Old method
# print("Введите число :")
# number = float(input())
# sum = 0
# for i in str(number):
#     if i != ".":
#         sum += int(i)
# print(f'Сумма чисел у введенного числа равна: {sum}.')

# New method
n = int(input('Введите число: '))
print(sum(map(int, str(n))))