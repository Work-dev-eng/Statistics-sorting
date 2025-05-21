data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
        element = float(input(f"Enter number {i+1}: "))
        data.append(element)

def insertionsort(data):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j], data[j-1]
        else:
            break
insertionsort(data) 
print(data)