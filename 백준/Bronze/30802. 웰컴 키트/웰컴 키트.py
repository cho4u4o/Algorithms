N = int(input())
t = list(map(int, input().split()))
T, P = map(int, input().split())

order = []
for i in t:
    num = i // T if i % T == 0 else i // T + 1
    order.append(num)

print(sum(order))
if N < P:
    print(0, N)
else:
    print(N // P, N % P)
