remainder = []
for i in range(10):
    k = int(input())
    remainder.append(k % 42)
print(len(list(set(remainder))))