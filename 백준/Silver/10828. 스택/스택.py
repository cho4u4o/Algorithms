class Stack:
    def __init__(self):
        self.stack = []
        self.peek = -1

    def push(self, item):
        self.stack.append(item)
        self.peek += 1

    def pop(self):
        if self.peek == -1:
            return -1
        else:
            result = self.stack[self.peek]
            self.stack.pop()
            self.peek -= 1
            return result

    def size(self):
        return self.peek + 1

    def empty(self):
        if self.peek == -1:
            return 1
        else:
            return 0

    def top(self):
        if self.peek == -1:
            return -1
        else:
            return self.stack[self.peek]


num = int(input())
stack = Stack()
result = []
for _ in range(num):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.push(cmd[1])
    elif cmd[0] == 'pop':
        result.append(stack.pop())
    elif cmd[0] == 'size':
        result.append(stack.size())
    elif cmd[0] == 'empty':
        result.append(stack.empty())
    elif cmd[0] == 'top':
        result.append(stack.top())
print(*result, sep="\n")
