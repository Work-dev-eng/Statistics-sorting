class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
d=int(input("Enter the fourth number: "))

Node1 = Node(a)
Node2 = Node(b)
Node3 = Node(c)
Node4 = Node(d)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

current = Node1
while current is not None:
    print(current.data, end ="->")
    current = current.next
print("None")