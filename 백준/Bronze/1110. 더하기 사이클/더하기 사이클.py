N = int(input())
firstN = N
add = int(N/10) + N % 10
N = N % 10 * 10 + add % 10
cnt = 1
if N == firstN:
    print(1)
else:
    while N != firstN:
        add = int(N / 10) + N % 10
        N = N % 10 * 10 + add % 10
        cnt = cnt + 1
    print(cnt)