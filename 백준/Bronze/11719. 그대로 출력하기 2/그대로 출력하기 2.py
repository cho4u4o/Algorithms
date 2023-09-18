while True:
    try:
        inputs = input()
        print(inputs)
    except EOFError:
        break