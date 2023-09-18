num = int(input())
for i in range(0, num):
    blankNum = num - (i+1)
    starNum = num - blankNum
    print(' '*blankNum + '*'*starNum)