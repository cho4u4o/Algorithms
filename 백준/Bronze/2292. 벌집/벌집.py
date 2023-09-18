N = int(input())

if N == 1:
    print(1)
    exit()

i = 0
num_sum = 1

while True:
    i += 1
    num_sum += i * 6
    if num_sum >= N:
        print(i + 1)
        exit()