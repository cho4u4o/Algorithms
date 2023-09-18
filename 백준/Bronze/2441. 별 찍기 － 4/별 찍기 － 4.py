num = int(input())
for i in range(0, num):
    blankNum = num - i
    starNum = num - blankNum
    print(' '*starNum + '*'*blankNum)