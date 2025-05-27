import sys
sys.setrecursionlimit(5)

print("This has been repeated", sys.getrecursionlimit(), "times")

def greet():
    print("Hey there!")
    greet()
print(greet)