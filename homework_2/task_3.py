# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

numbs = list(range(1,int(input('Введите n '))+1))
result = 0

for i in numbs:
    result +=(1+1/i)**i

print(result)