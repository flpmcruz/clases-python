

def repetidos(*args):
    cero = False

    for n in args:
        if n == 0 and cero is True:
            return True

        elif n == 0:
            cero = True

        else:
            cero = False

    return False


print(repetidos(5, 6, 1, 0, 0, 9, 3, 5))  # return true
print(repetidos(6, 0, 5, 1, 0, 3, 0, 1))  # return false
