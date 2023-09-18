num = int(input())
for i in range(1, num):
    if sum(list(map(int, str(i)))) + i == num:
        print(i)
        exit()
print(0)