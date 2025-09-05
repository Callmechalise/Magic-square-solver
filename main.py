import numpy as np
shells=9
numbers=[i for i in range(1,shells**2+1)]
print(numbers)
matrix=np.zeros((shells,shells))
print(matrix)
i=0
j=shells//2
matrix[i][j]=numbers[0]

def solve(i,j,n):
    totalsum=0
    k = 1
    while (totalsum!=(sum(numbers))) and k<len(numbers):
        next_i = (i - 1) % n
        next_j = (j + 1) % n
        if matrix[next_i][next_j] != 0:
            next_i = (i + 1) % n
            next_j = j

        matrix[next_i][next_j]=numbers[k]
        k+=1
        totalsum=np.sum(matrix)
        i, j = next_i, next_j
solve(i,j,shells)
print(matrix)
