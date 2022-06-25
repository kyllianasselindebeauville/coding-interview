# 1.8 Zero Matrix

from typing import List


def set_zeros(matrix: List[List[int]]) -> None:
    """If an element of a matrix is 0, its entire row and column are set to 0.

    Iterates through each cell and keeps the row and column when there is a 0
    to nullify the corresponding rows and columns.

    Args:
        matrix: An M x N matrix of integers.

    Returns:
        None.
    """
    rows, cols = set(), set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(len(matrix[row])):
            matrix[row][j] = 0

    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0


def main():
    m = int(input('Enter the number of rows: '))
    n = int(input('Enter the number of columns: '))
    matrix = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(input(f'Enter a number for ({i},{j}): '))

    print('\nMatrix:', *matrix, sep='\n')

    set_zeros(matrix)

    print('\nResult:', *matrix, sep='\n')


if __name__ == '__main__':
    main()
