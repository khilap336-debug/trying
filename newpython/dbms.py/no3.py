
n=int(input("enter a number : "))
a=[]
for i in range(n):
    x=int(input("enetr the elements : "))
    a.append(x)
    print(a)

y=int(input("enter the number you want to pop : "))
a.pop(y)
print(a)

