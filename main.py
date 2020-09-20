#! /usr/bin/env python3
# © 2020 Cristiano Migali

# returns the index j of the pivot in row and True if there is a pivot,
# otherwise it returns 0 and False
def j_pivot(row):
    for j in range(len(row)):
        if row[j] != 0:
            return j, True
    return 0, False

# returns the linear_combination row_i + t * row_j
def linear_combination(row_i, row_j, t):
    if len(row_i) != len(row_j):
        print('error: row_i and row_j must have the same length')
        exit(1)

    comb = [0] * len(row_i)
    for i in range(len(row_i)):
        comb[i] = row_i[i] + t * row_j[i]
    
    return comb

# returns the index of the first row, starting from top, with the leftmost pivot
def i_row_leftmost_pivot(matrix):
    i_leftmost_pivot, j_leftmost_pivot = 0, len(matrix[0])
    for i in range(len(matrix)):
        row = matrix[i]
        j_pivot_row, pivot_exists = j_pivot(row)
        if j_pivot_row < j_leftmost_pivot and pivot_exists:
            j_leftmost_pivot = j_pivot_row
            i_leftmost_pivot = i
    
    return i_leftmost_pivot

# return True if the matrix is a stair matrix,
# otherwise it return False
def is_stair(matrix):
    j_pivot_row_before = -1
    for row in matrix:
        j_pivot_row, pivot_exists = j_pivot(row)
        if not pivot_exists:
            j_pivot_row_before = len(row)
        elif j_pivot_row <= j_pivot_row_before:
                return False
        else:
            j_pivot_row_before = j_pivot_row
    
    return True

# main part of gaussian elimination algorithm
def elimination(matrix):
    if is_stair(matrix):
        return matrix
    
    i_to_swap = i_row_leftmost_pivot(matrix)
    matrix[0], matrix[i_to_swap] = matrix[i_to_swap], matrix[0]

    j_pivot_first_row, pivot_exists = j_pivot(matrix[0])

    if not pivot_exists:
        print('error: if first row has no pivot, and the first line row is the one with the leftmost pivot, matrix should be a stair matrix')
        exit(1)

    for i in range(1, len(matrix)):
        j_pivot_row_i, pivot_exists = j_pivot(matrix[i])

        if not pivot_exists:
            continue

        if j_pivot_row_i < j_pivot_first_row:
            print('error: first row should have the leftmost pivot')
            exit(1)
        
        if j_pivot_row_i == j_pivot_first_row:
            matrix[i] = linear_combination(matrix[i], matrix[0], -1 * matrix[i][j_pivot_row_i] / matrix[0][j_pivot_first_row])
    
    stair_matrix = [matrix[0]]
    stair_matrix.extend(elimination(matrix[1:]))
    return stair_matrix

# pretty print of the matrix
def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print('%.2f\t' % elem, end='')
        print()

def main():
    m = int(input('Insert number of rows: '))
    n = int(input('Insert number of columns: '))
    print('Insert matrix')

    matrix = []
    for i in range(m):
        line = input()
        str_row = line.split(' ')
        
        if len(str_row) != n:
            print('error: the line %i has not n element' % i)
            exit(1)
        
        matrix.append([])
        for j in range(n):
            matrix[-1].append(float(str_row[j]))
    
    matrix = elimination(matrix)
    print_matrix(matrix)

if __name__ == '__main__':
    main()
        