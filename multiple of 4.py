import numpy as np
def create_doubly_even_magic_square(n):
    matrix = np.zeros((n, n), dtype=int)
    num = 1

    # Create pattern
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4) + (j % 4) == 3):
                matrix[i][j] = num
            else:
                matrix[i][j] = n * n + 1 - num
            num += 1
    return matrix
print(create_doubly_even_magic_square(4))