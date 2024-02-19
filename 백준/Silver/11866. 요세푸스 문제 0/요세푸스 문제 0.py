from collections import deque

n, k = map(int, input().split())
result = []
queue = deque(range(1, n + 1))
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')