# 1.7 Rotate Matrix

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """Rotates an integer matrix by 90 degrees.

    Iterates through each cell and assign the value of another cell to rotate
    the matrix.

    Args:
        matrix: An N x N matrix of integers.

    Returns:
        None.
    """
    size = len(matrix)
    rotated = [[None for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[i][j] = matrix[size - 1 - j][i]
    matrix[:] = rotated[:]

def main():
    size = int(input('Enter the size of the matrix: '))
    matrix = [list() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i].append(int(input(f'Enter a number for ({i},{j}): ')))

    print('\nMatrix:')
    for i in range(size):
        print(matrix[i])

    rotate(matrix)

    print('\nRotated matrix:')
    for i in range(size):
        print(matrix[i])

if __name__ == '__main__':
    main()
