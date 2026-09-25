
n = int(input("Enter number of elements in first list: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

m = int(input("Enter number of elements in second list: "))
b = []

for i in range(m):
    x = int(input("Enter element: "))
    b.append(x)

a.extend(b)

print("Extended list:", a)



