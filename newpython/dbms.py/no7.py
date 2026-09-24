
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

x = int(input("Enter element to find: "))

if x in a:
    pos = a.index(x)
    print("Element found at index:", pos)
else:
    print("Element not found")

