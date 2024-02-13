nums = list(map(int, input().split()))
biggest = 0
differ = [0, 0, 0]
for i in range(0, 3):
    if nums[i] >= biggest:
        biggest = nums[i]
big = biggest
for i in range(0, 3):
    differ[i] = biggest - nums[i]
    if differ[i] != 0 and differ[i] < big:
        big = differ[i]
result = biggest - big
if nums[0] == nums[1] or nums[0] == nums[2]:
    result = nums[0]
elif nums[1] == nums[2]:
    result = nums[1]
else:
    result = biggest - big
print(result)