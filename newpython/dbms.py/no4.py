n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

print("List:", a)

y = int(input("Enter element you want to search: "))

if y in a:
    print("Element found at index:", a.index(y))
else:
    print("Element not found")