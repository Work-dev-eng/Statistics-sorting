data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
        element = float(input(f"Enter number {i+1}: "))
        data.append(element)

def quicksort(data):
        if len(data) <= 1:
                return data
        
        p = data[-1]

        L = [x for x in data[:-1] if x <= p]
        R = [x for x in data[:-1] if x > p]

        L = quicksort(L)
        R = quicksort(R)

        return L + [p] + R
quicksort(data)
print(data)