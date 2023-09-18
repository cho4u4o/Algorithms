scores = []
for i in range(0, 5):
    score = int(input())
    if score < 40:
        score = 40
    scores.append(score)
print(int(sum(scores) / 5))
