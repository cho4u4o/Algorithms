class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[0]

    def back(self):
        if len(self.items) == 0:
            return -1
        else:
            return self.items[-1]


num = int(input())
queue = Queue()
result = []
for _ in range(num):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.push(cmd[1])
    elif cmd[0] == 'pop':
        result.append(queue.pop())
    elif cmd[0] == 'size':
        result.append(queue.size())
    elif cmd[0] == 'empty':
        result.append(queue.empty())
    elif cmd[0] == 'front':
        result.append(queue.front())
    elif cmd[0] == 'back':
        result.append(queue.back())
print(*result, sep="\n")
