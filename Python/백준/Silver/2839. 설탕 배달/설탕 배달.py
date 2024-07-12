def cap5(num):
    if num % 5 == 0:
        return num // 5
    else:
        return cap35(num)


def cap35(num):
    ininum = num
    cnt5 = 0
    while num > 2:
        num -= 5
        cnt5 += 1
        if num % 3 == 0:
            if num // 3 < 5:
                cnt3 = num // 3
                return cnt5 + cnt3
            elif num // 3 > 5:
                continue
    return cap3(ininum)


def cap3(num):
    if num % 3 == 0:
        return num // 3
    else:
        return -1


num = int(input())
print(cap5(num))
