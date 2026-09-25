n = int(input("Enter number of elements: "))
a = []

for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)

b = a.copy()

print("Original list:", a)
print("Copied list:", b)


