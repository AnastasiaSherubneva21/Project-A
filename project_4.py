# Word creature

import random
from os import remove

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


# Word solving
