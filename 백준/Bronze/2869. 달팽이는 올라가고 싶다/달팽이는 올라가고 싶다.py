A, B, V = map(int, input().split())
leftover = V - A
one_day = A - B

if leftover % one_day == 0:
    print(int(leftover / one_day) + 1)
else:
    print(int(leftover / one_day) + 2)