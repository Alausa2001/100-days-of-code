#!/usr/bin/python3
from random import seed, shuffle, choice
lett =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 's', 'T', 'u'
'V', 'w', 'X', 'y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['!', '#', '@', '$', '&', '%']
no_lett = int(input("Enter the no of alphabets you want in your password\n"))
no_num = int(input("Enter the no of digits you want\n"))
no_special =int(input("Enter the no of special characters you want\n"))
seed()
password = ""
for a in range(0, no_lett):
    no1 = choice(lett)
    password += no1
for a in range(0, no_num):
    no2 = choice(num)
    password += no2
for a in range (0, no_special):
    no3 = choice(special)
    password += no3
password = list(password)
result = ''
shuffle(password)
for a in password:
    result += a
print("Your password is {}".format(result))
