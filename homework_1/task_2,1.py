#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 1
y = 0
z = 0
if not(x and y and z) ==  ~x and ~y and ~z:
    print('true')
else:
    print('false')