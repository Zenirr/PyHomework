# Реализуйте алгоритм перемешивания списка.
import random

numb_list = list(range(int(input('Введите число элементов - '))))
print(numb_list)
random.shuffle(numb_list)
print(numb_list)