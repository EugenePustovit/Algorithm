
def insertion_sort_inc(a):

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1

        a[i+1] = key

    print(a)


def insertion_sort_dec(a):

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i -= 1

            print('while loop - [{}]'.format(a))

        a[i+1] = key

    print(a)


def searching_problem(a, v):
    for index, item in enumerate(a):
        if item == v:
            return index

    return None


def adding_two_binaries(a, b):
    c = [0]*(len(a)+1)

    mem = 0
    for i in range(1, len(a)+1):
        buf = a[-i] ^ b[-i]
        c[-i] = buf ^ mem

        if (a[-i] & b[-i]) or (mem & buf):
            mem = 1
        else:
            mem = 0
    c[0] = mem

    return c


if __name__ == "__main__":
#    a = [5, 2, 4, 6, 1, 3]
#    a = [31, 41, 59, 26, 41, 58]
#    insertion_sort_dec(a)

#    res = searching_problem(a, 2)
#    print(res)

    a = [0, 1, 1, 1]
    b = [1, 1, 1, 1]

    print(a)
    print(b)
    res = adding_two_binaries(a, b)
    print(res)
