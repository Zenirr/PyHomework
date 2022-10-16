# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from fileinput import close
import random 

N = int(input('Введите число элементов - '))
rand_list = []
new_list = []
multip = 1

count = 0
while count<N:
    rand_list.append(random.randint(-N,N))
    count +=1

print(rand_list)


data = open('../file.txt','r')

for line in data:
    if -len(rand_list)<= int(line) < len(rand_list):
        multip*=rand_list[int(line)]
        new_list.append(rand_list[int(line)])
data.close()

print(new_list)
print(multip)