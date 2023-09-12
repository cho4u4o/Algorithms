word = list(map(ord, input().upper()))
wordOppo = list(set(word))
wordCnt = list(map(word.count, wordOppo))
OppoCnt = dict(zip(wordOppo, wordCnt))
CntOppo = {wordCnt: wordOppo for wordOppo, wordCnt in OppoCnt.items()}
wordCnt.sort()
if len(wordOppo) == 1:
    print(chr(wordOppo[0]))
elif wordCnt[len(wordCnt) - 1] == wordCnt[len(wordCnt) - 2]:
    print('?')
else:
    print(chr(CntOppo[wordCnt[len(wordCnt) - 1]]))
