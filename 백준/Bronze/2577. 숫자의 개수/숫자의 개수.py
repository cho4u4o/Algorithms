A = int(input())
B = int(input())
C = int(input())
multiple = A * B * C
result = list(map(int, list(str(multiple))))
for i in range(0, 10):
    print(int(result.count(i)))