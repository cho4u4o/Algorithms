import sys

n = int(sys.stdin.readline())
arr = [0] * (10000 + 1)
for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)