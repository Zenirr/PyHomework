# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

n = int(input('\nВведите натуральное число которое будут степенью = '))
result = []
def rand():
    return random.randint(0,100)

for i in range(n,1,-1):
    c = 0
    if c:
        result.append(f'{c}x^{i}')

c = 1
if c:
    result.append(f'{c}x')

c = 2
if c:
    result.append(f'{c}')

result_lst = ' + '.join(result) + ' = 0'

with open('polynumbers.txt', 'a') as file:
    file.write( result_lst +'\n')
    
print(result_lst)