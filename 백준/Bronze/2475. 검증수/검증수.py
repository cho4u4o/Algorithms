nums = list(map(int, input().split()))


def func_pow(x):
    return pow(x, 2)


squares = list(map(func_pow, nums))
print(sum(squares) % 10)
