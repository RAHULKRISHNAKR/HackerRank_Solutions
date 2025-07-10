'''Solve this problem with a complexity less than m+n.

Read the following input: an integer n representing the number of rows in the matrix, and an integer m representing the number of columns in the matrix and the values of the matrix (n rows and m columns).

The matrix is sorted such that all elements in any row are sorted in increasing order from left to right, and all elements in any column are sorted in increasing order from top to bottom. You should print the total number of negative numbers present in the matrix.

The input will be provided as follows:

The first line of input contains a single integer n, the number of rows in the matrix.
The second line of input contains a single integer m, the number of columns in the matrix.
The next n lines each contain m integers separated by spaces, representing the elements of the matrix.
Solve this problem with a complexity less than m+n.'''

row = int(input())
col = int(input())

mat=[]
for _ in range(row):
    mat.append(list(map(int, input().split())))
    

i = row - 1  
j = 0
count = 0

while i >= 0 and j < col:
    if mat[i][j] <= 0:
        count += i + 1  
        j += 1
    else:
        i -= 1

print(count)

