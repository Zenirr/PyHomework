# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
N = int(input('Введите количество элементов = '))
fibonacci = []
minus_fibonacci = []

for i in range(N+1):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

for i in range(N,0,-1):
    minus_fibonacci.append(((-1)**(i+1))*fibonacci[i])

print(f'Для К = {N}')
print(minus_fibonacci + fibonacci)