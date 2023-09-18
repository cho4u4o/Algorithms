N = int(input())
for i in range(0, N):
    a, word = map(str, input().split())
    for k in range(0, len(word)):
        print(list(word)[k] * int(a), end='')
    print('\n', end='')
