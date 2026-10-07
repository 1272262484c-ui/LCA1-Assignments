# Assignment 4: Addition of Two Matrices

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")
A = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter A[{i}][{j}]: "))
        row.append(value)
    A.append(row)

print("\nEnter elements of Matrix B:")
B = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter B[{i}][{j}]: "))
        row.append(value)
    B.append(row)

# Matrix addition
C = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResultant Matrix:")
for row in C:
    print(row)
