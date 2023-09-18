num = int(input())

for i in range(num):
    exam = list(map(int, input().split()))
    del exam[0]
    aver = sum(exam)/len(exam)
    count = 0
    for j in exam:  
        if j > aver:
            count += 1
    print("%.3f%%" % (count/len(exam)*100))