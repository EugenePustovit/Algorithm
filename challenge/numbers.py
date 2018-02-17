
def numbers(n=10):
    for i in range(1, n+1):
        res = []
        for j in range(1, n+1):
            res.append(str(j*i))

        print(' '.join(res))


def numbers_(n=10):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(j*i, end='\t')

        print()


if __name__ == "__main__":
    numbers_()
