numbers = list(map(int, input().split()))
result = numbers[0]
for i in numbers[1:]:
    result = result - i
print(result)