
n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

x = int(input("Enter element to delete: "))

if x in a:
    a.remove(x)
    print("List after deletion:", a)
else:
    print("Element not found")


