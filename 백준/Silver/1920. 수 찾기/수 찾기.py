import sys

def bin_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가운데 값

    # 원하는 값 찾을 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점 값보다 타겟이 작을 경우
    elif array[mid] > target:
        return bin_search(array, target, start, mid - 1)
    # 중간점 값보다 타겟이 클 경우
    else:
        return bin_search(array, target, mid + 1, end)


n = int(sys.stdin.readline())
nums = [int(x) for x in input().split()]
m = int(sys.stdin.readline())
compare = [int(x) for x in input().split()]
nums.sort()
for i in range(m):
    if compare[i] > nums[n - 1]:
        print(0)
    elif compare[i] == nums[n - 1] or compare[i] ==  nums[0]:
        print(1)
    elif compare[i] < nums[n - 1]:
        if bin_search(nums, compare[i], 0, n - 1):
            print(1)
        else:
            print(0)

