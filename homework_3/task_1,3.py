# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

array =  [1.54, 3.14, 4.12, 3.3, 20.42, 13.042]
min = 1
max = 0

for i in array:
    i = str(i)
    i = i.split('.')
    part = int(i[1])/10**len(i[1])
    if part > max:
        max = part
    if part < min:
        min = part

print(f'Максимум = {max} Минимум = {min}')
print(f'Разница = {round(max-min,4)}')