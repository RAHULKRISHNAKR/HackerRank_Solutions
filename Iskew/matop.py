'''Imagine you are helping a student with their mathematics homework which involves a lot of problems based on matrix addition. You decide to write a program to automate the task of adding two matrices, which would make the homework a breeze!

Write a program to add two matrices. The program should:

Prompt the user to enter the dimensions of the matrices (assume both matrices have the same dimensions).

Accept the elements of the two matrices from the user.

Display the two matrices.

Add the two matrices.

Print the resultant matrix.'''

# Read matrix dimensions
row, col = map(int, input().split())

# Read Matrix 1
mat1 = []
for _ in range(row):
    mat1.append(list(map(int, input().split())))

# Read Matrix 2
mat2 = []
for _ in range(row):
    mat2.append(list(map(int, input().split())))

# Print First Matrix
print("First Matrix:")
for i in range(row):
    for j in range(col):
        print(mat1[i][j], end=" ")
    print()

# Print Second Matrix
print("Second Matrix:")
for i in range(row):
    for j in range(col):
        print(mat2[i][j], end=" ")
    print()

# Calculate and Print Result Matrix
print("Sum of the two matrices is:")
for i in range(row):
    for j in range(col):
        print(mat1[i][j] + mat2[i][j], end=" ")
    print()
