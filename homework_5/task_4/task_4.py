# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст который нужно сжать: '))
with open('words.txt', 'r') as file:
    my_txt = file.readline()
    txt_compressed = my_txt.split()

print(my_txt)

def file_encod(txt):
    encod = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encod += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encod += str(count) + prev_char
        return encod


txt_compressed = file_encod(my_txt)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compressed}')
print(txt_compressed)