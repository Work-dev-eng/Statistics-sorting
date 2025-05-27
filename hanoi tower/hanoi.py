def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print("move 1st disk from ", a, " to", c )
        return
    tower_of_hanoi(n -1, a, c, b)
    print("Move", n, "th disk from", a, " to", c)
    tower_of_hanoi(n - 1, b, a , c)

print(tower_of_hanoi(4, "a", "b", "c"))