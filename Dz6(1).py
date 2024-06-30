import string
import random

userPass = ""
x = string.ascii_uppercase
y = string.ascii_lowercase
n = string.digits
m = string.punctuation

user_len = int(input("Enter len\t"))
userChoise = input("Enter what you want choose u=upp,l=low,d=digits,p=punctuation\t")

if userChoise=="u":
    for i in range(user_len):
        userPass+=random.choice(x)
        print(userPass)
if userChoise=="l":
    for i in range(user_len):
        userPass+=random.choice(y)
        print(userPass)
if userChoise=="d":
    for i in range(user_len):
        userPass+=random.choice(n)
        print(userPass)
if userChoise=="p":
    for i in range(user_len):
        userPass+=random.choice(m)
        print(userPass)
if userChoise=="ul":
    for i in range(user_len):
        userPass+=random.choice(x+y)
        print(userPass)
if userChoise=="ud":
    for i in range(user_len):
        userPass+=random.choice(x+n)
        print(userPass)
if userChoise=="up":
    for i in range(user_len):
        userPass+=random.choice(x+m)
        print(userPass)
if userChoise=="ld":
    for i in range(user_len):
        userPass+=random.choice(y+n)
        print(userPass)
if userChoise=="lp":
    for i in range(user_len):
        userPass+=random.choice(y+m)
        print(userPass)
if userChoise=="dp":
    for i in range(user_len):
        userPass+=random.choice(n+m)
        print(userPass)
if userChoise=="uld":
    for i in range(user_len):
        userPass+=random.choice(x+y+n)
        print(userPass)
if userChoise=="ulp":
    for i in range(user_len):
        userPass+=random.choice(x+y+m)
        print(userPass)
if userChoise=="udp":
    for i in range(user_len):
        userPass+=random.choice(x+n+m)
        print(userPass)
if userChoise=="ldp":
    for i in range(user_len):
        userPass+=random.choice(y+n+m)
        print(userPass)
if userChoise=="uldp":
    for i in range(user_len):
        userPass+=random.choice(x+y+n+m)
        print(userPass)



