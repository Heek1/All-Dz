def x():
    num=int(input("Enter number: "))
    for i in range(1,101):
        print(num,"x",i,"=",num*i)
x()

def y(st):
    print(len(st))
st=input("Enter string: ")
y(st)

def b(stt):
    if stt==stt.upper():
       Newsttlo=stt.lower()
       print(Newsttlo)
    if stt==stt.lower():
       Newsttup=stt.upper()
       print(Newsttup)
stt=input("Enter string: ")
b(stt)

def g(number1,number2,number3):
    number=(number1+number2+number3)/3
    print(number)
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))
g(number1,number2,number3)

def f(num1,num2,num3):
    numm= max(num1,num2,num3)
    print(numm)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
f(num1,num2,num3)