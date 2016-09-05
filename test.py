def factorial(num):
    i = 1
    factoria = 1
    if num == 0:
        return 1

    elif num > 0:
        while i <= num:
            factoria = factoria * i
            i = i + 1
        return factoria

    else:
        return "No factorial!"


print factorial(0)
print factorial(-3)
print factorial(3)
