data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
        element = float(input(f"Enter number {i+1}: "))
        data.append(element)
def bubble(data):
     n=len(data)
     flag=True
     while flag:
            flag=False
            for i in range (1,n):
                   if data [i-1]>data[i]:
                          flag=True
                          data [i-1],data[i] = data[i],data [i-1]
bubble(data)
print(data)