
from math import *

premier = input('Entrer premier nombre')

A = str(input('Entrer le signe de l''opération : + , - , / , * '))

second = input('Entrer second nombre')

if A == "+":
    print (int(premier)+int(second))

elif A == "-":
    print(int(premier)-int(second))

elif A == "/":
    print(int(premier)/int(second))

elif A == "*":
    print(int(premier)*int(second))