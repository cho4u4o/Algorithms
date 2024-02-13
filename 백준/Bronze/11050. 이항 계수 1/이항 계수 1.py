n, k = map(int, input().split())


def factorial(x):
    result = 1
    for i in range(0, x):
        result = result * (i + 1)
    return result

print(int(factorial(n) / (factorial(n-k) * factorial(k))))