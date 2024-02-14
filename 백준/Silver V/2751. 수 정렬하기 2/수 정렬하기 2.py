import sys

n = int(sys.stdin.readline())
nums = []
for i in range(0, n):
    a = int(sys.stdin.readline())
    nums.append(a)
nums = list(sorted(nums))
print(*nums, sep='\n')