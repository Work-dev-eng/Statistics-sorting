while True:
        data = []
        n = int(input("Enter the number of objects present: "))
        for i in range(n):
            element = float(input(f"Enter number {i+1}: "))
            data.append(element)

        def mode(data):
            maxcount=(0,0)
            for num in data:
                occurances = data.count(num)
                if occurances > maxcount[0]:
                    maxcount= (occurances, num)
            return maxcount[0]
        print(mode(data))

        repeat = input("Please type 'NO' if you want to exit the program")
        if repeat == "NO":
            break