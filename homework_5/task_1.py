#Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

txt = input("Введите текст: ")
print(f"Исходный текст: {txt}")
find_txt = "абв"
txt_list = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(txt_list)}')