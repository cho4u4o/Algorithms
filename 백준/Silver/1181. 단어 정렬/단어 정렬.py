n = int(input())
words = []
for i in range(0, n):
    words.append(input())  # 단어 입력받기
words = list(set(words))
words = sorted(words)
words.sort(key=len)
for j in range(0, len(words)):
    if j == len(words) - 1 :
        print(words[j], end='')
    else:
        print(words[j])