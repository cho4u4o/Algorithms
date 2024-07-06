class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.top = None

    def push(self, item):
        self.stack.append(item)
        self.size += 1
        self.top = self

    def pop(self):
        result = self.stack[self.size - 1]
        self.size -= 1
        self.top = self.stack[self.size - 1]
        return result

    def is_empty(self):
        if self.size == 0:
            return True


num = int(input())
for i in range(num):
    q = input()
    stack = Stack()
    qAnswer = True
    for j in q:
        if j == "(":
            stack.push(j)
        elif j == ")":
            if stack.is_empty():
                print("NO")
                qAnswer = False
                break
            else:
                stack.pop()
    if not qAnswer:
        continue
    if stack.is_empty():
        print("YES")
    else:
        print("NO")
