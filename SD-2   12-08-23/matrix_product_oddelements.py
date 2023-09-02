'''product of odd elements of a sqaure matrix whose i th and jth values
are same'''
def product_odd_diagonal_elements(matrix):
    n = len(matrix)
    total = 1
    
    for i in range(n):
        if matrix[i][i] % 2 == 1:  # Check if i-th and j-th values are odd and equal
            total *= matrix[i][i]
    
    return total

# Example square matrix
matrix = [
    [1, 2, 3],
    [4, 4, 6],
    [7, 8, 9]
]

result = product_odd_diagonal_elements(matrix)
print("product of odd diagonal elements:", result)
