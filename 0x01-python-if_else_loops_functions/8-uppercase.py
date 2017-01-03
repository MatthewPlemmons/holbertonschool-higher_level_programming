def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            c = ord(c) - 32
            print(chr(c), end="")
        else:
            print(c, end="")
    print("")
