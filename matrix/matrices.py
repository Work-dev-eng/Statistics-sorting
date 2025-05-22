import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))


def input_matrix(name):
    print(f"Enter the elements of matrix {name} row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} integers.")
            row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)


a = input_matrix("A")
b = input_matrix("B")

c = a + b
print("Resultant Matrix after addition:")
print(c)