
def find_smallest_element(a):
    pass


def selection_sort(a):
    for i in range(0, len(a)-1):
        min_index = i
        for index in range(i+1, len(a)):
            if a[index] < a[min_index]:
                min_index = index

        if min_index != i:
            a[min_index], a[i] = a[i], a[min_index]

    return a


if __name__ == "__main__":
    a = [5, 2, 4, 6, 1, 3]
#    a = [31, 41, 59, 26, 41, 58]

    res = selection_sort(a)
    print(res)
