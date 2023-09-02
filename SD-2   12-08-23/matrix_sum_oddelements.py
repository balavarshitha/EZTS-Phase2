'''write a python program for the addition of odd elements of a square
matrix whos i th and j th value will be the same'''
def add_odd_diagonal_elements(matrix):
    n = len(matrix)
    total = 0
    
    for i in range(n):
        if matrix[i][i] % 2 == 1:  # Check if i-th and j-th values are odd and equal
            total += matrix[i][i]
    
    return total

# Example square matrix
matrix = [
    [1, 2, 3],
    [4, 4, 6],
    [7, 8, 9]
]

result = add_odd_diagonal_elements(matrix)
print("Sum of odd diagonal elements:", result)
