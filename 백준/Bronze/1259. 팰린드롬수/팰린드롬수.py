while True:
    nums = list(map(int, input()))
    if nums == [0]:
        exit()
    else:
        if nums == list(reversed(nums)):
            print('yes')
        else:
            print('no')