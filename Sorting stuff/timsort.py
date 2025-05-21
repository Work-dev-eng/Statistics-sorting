from mergesort import merge_sort
from insertiontest import insertionsort

data = []
n = int(input("Enter the number of objects present: "))
for i in range(n):
    element = float(input(f"Enter number {i+1}: "))
    data.append(element)

MIN_RUN = 32

def tim(arr):
    n = len(arr)
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertionsort(arr, start, end)

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge_sort(arr, left, mid, right)
        size *= 2

tim(data)

print("Sorted data:")
print(data)