import numpy as np

rows = int(input("Please enter the number of rows: "))
cols = int(input("Please enter the number of columns: "))

def input_matrix(name):
    matrix = []
    if name == "A":
        print(f"\nEnter the elements of matrix {name} row by row (separated by spaces):")
        for i in range(rows):
            while True:
                try:
                    row = list(map(int, input(f"Row {i+1}: ").split()))
                    if len(row) != cols:
                        raise ValueError
                    matrix.append(row)
                    break
                except ValueError:
                    print(f"Please enter exactly {cols} integers.")
    elif name == "B":
        print(f"\nEnter the elements of matrix {name} one by one:")
        for i in range(rows):
            row = []
            for j in range(cols):
                while True:
                    try:
                        value = int(input(f"Element at row {i+1}, column {j+1}: "))
                        row.append(value)
                        break
                    except ValueError:
                        print("Please enter a valid integer.")
            matrix.append(row)
    return np.array(matrix)

a = input_matrix("A")
b = input_matrix("B")

c = a + b

print("\nMatrix A:")
print(a)
print("\nMatrix B:")
print(b)
print("\nResultant Matrix after addition:")
print(c)
