A = [[0, 0], [0, 0]]
B = [[0, 0], [0, 0]]
C = [[0, 0], [0, 0]]

print("Enter elements of Matrix A:")

for i in range(2):
    for j in range(2):
        A[i][j] = int(input("Enter element: "))

print("Enter elements of Matrix B:")

for i in range(2):
    for j in range(2):
        B[i][j] = int(input("Enter element: "))

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]

print("\naddition of matrices is:")

for i in range(2):
    print(C[i])

