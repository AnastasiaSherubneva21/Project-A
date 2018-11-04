
import random
from os import remove

e = None
while e != 0:

    letters = ['А', 'Е', 'Н', 'О', 'С', 'Т']
    a = random.choice(letters)
    letters.remove(a)
    b = random.choice(letters)
    letters.remove(b)
    c = random.choice(letters)
    letters.remove(c)
    d = random.choice(letters)
    letters.remove(d)

    list_word = [a, b, c, d]
    str_word = (str(a+b+c+d))

    print('Загадано четырехбуквенное слово из букв А, Е, Н, О, С, Т.')
    print('Отгадай!')

    for i in range(10):
        s = 0
        ch = 0
        print('Попытка №', (i+1), ':', end=' ')
        x = str(input())

        if a == x[0]:
            s += 1
        else:
            y = x[1:]
            ch_11 = y.find(a)
            if ch_11 > -1:
                ch += 1

        if b == x[1]:
            s += 1
        else:
            y = x[:1]
            ch_21 = y.find(b)
            z = x[2:]
            ch_22 = z.find(b)
            if ch_21 > -1 or ch_22 > -1:
                ch += 1

        if c == x[2]:
            s += 1
        else:
            y = x[:2]
            ch_31 = y.find(c)
            z = x[3:]
            ch_32 = z.find(c)
            if ch_31 > -1 or ch_32 > -1:
                ch += 1

        if d == x[3]:
            s += 1
        else:
            y = x[:3]
            ch_41 = y.find(d)
            if ch_41 > -1:
                ch += 1

        print('На "своем месте":', s)
        print('На "чужом месте":', ch)
        if s == 4:
            break

    if s == 4:
        print('Вы выиграли!')
    else:
        print('Вы проиграли! Загаданное слово -', str_word)

    print('Хотите сыграть еще раз? Для продолжения введите "1", для выхода - "0"')
    e = int(input())

print('Сеанс завершен!')
