N = int(input())
scores = {}
count = 0
scoCnt = []
for i in range(0, N):
    scores[i] = list(input())
for i in range(0, N):
    for n in scores[i]:
        if n == 'O':
            count = count + 1
            scoCnt.append(count)
        else:
            count = 0
            scoCnt.append(count)
    scores[i] = sum(scoCnt)
    count = 0
    scoCnt = []
for i in range(0, N):
    print(scores[i])