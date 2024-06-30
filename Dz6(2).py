import random
sum=0
x = random.randint(1,101)
while True:
   y = int(input("Enter number\t"))
   if x > y:
    print("загадкове число більше")
   sum += 1
   if x < y:
    print("загадкове число менше")
    sum += 1
   if x==y:
    print("Ви виграли" )
    sum += 1
    print(f"за {sum} спроб")
    break
