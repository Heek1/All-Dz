x=[0,0,1,4,4,-6,-2,-6,7]
y=x[0]
for i in x[::-1]:
   if i < 0 :
       y=i
       p=x[::-1].index(i)
       print(f"Останній  від'ємний елемент: {i}")
       print(f"Його індекс: {p}")
       break

