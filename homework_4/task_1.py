# Вычислить число c заданной точностью d

import random

number = random.uniform(1,5)
degree = random.randint(-10,-1)
d = 10 ** degree

result = round(number, -degree)
print(f'Число {number} было округлено с точностью {d}, и получилось число {result}')