while True:
    data = []
    n = int(input("Enter the number of objects present: "))
    for i in range(n):
        element = float(input(f"Enter number {i+1}: "))
        data.append(element)


    def mean(data):
        total = 0
        for num in data:
            total=total+num
        return total/len(data)
    print(mean(data))

    repeat = input("Please enter 'NO' if you do not want to repeat the processs or enter 'YES' if you want to redo the process: ")
    if repeat == "NO":
     break

