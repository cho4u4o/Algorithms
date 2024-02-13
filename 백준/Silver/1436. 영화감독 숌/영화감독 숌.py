x = int(input())
num = 665  # 하나씩 올려서 조건에 만족하는 수를 저장할 변수
cnt = 0  # 6의 개수를 세고 저장할 변수, 6이 연속으로 3개 나와야 함
sequency = 0  # 6을 3개 가지고 있는 수 중에서 몇 번째로 큰 수인가?
while True:
    num = num + 1
    nums = str(num)
    if '666' in nums:
        cnt = cnt + 1
    if cnt == 1:
        sequency = sequency + 1
    cnt = 0
    if sequency == x:
        break
print(num)