# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
d = 0
while d < len(my_list):
    number = my_list[d]
    d = d + 1
    if number == 0:
        continue
    elif number < 0:
        break
    else:
        print(number)