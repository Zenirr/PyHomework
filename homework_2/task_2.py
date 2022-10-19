# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

numbs = list(range(1,int(input('Введите N '))+1))
result = 1
for i in numbs:
    result *=i
    print(result)