import math
N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in range(0, N):
    if nums[i] == 1:
        continue
    elif nums[i] == 2:
        count += 1
    else:
        is_prime = True
        for j in range(2, int(math.sqrt(nums[i])) + 1):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
print(count)