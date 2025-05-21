data = []

# Get the number of elements
n = int(input("Enter the number of objects present: "))

# Append elements to the list
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))  # Convert input to float
    data.append(element)

def median(data):
    data.sort()
    N = len(data)

    if N % 2 == 1:
        return data[N // 2]
    else:
        a = data[N // 2 - 1]
        b = data[N // 2]
        return (a + b) / 2

print("The median is:", median(data))
