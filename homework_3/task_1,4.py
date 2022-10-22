# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = int(input('Введите десятичное число = '))
print(f'Десятичное число = {number}')
binar = ''

while number > 0:
    prev_number = number%2
    number //= 2
    binar = str(prev_number) + binar

print(f'Двоичное число = {binar}')