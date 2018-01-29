
def merge_example(a_list, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    l_list, r_list = []
    for i in range(0, n1):
        l_list.append(a_list[p+i])
    for j in range(0, n2):
        r_list.append(a_list[q+j+1])

    l_list[n1+1], r_list[n2+1] = 'infinity'
    i = 0
    j = 0
    for k in range(p, r+1):
        if l_list[i] <= r_list[j]:
            a_list[k] = l_list[i]
            i += 1
        else:
            a_list[k] = r_list[j]
            j += 1


def merge_list(a_list, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    l_list = [a_list[p+i] for i in range(n1)]
    r_list = [a_list[q+j+1] for j in range(n2)]

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if l_list[i] <= r_list[j]:
            a_list[k] = l_list[i]
            i += 1
        else:
            a_list[k] = r_list[j]
            j += 1
        k += 1

    while i < n1:
        a_list[k] = l_list[i]
        k += 1
        i += 1

    while j < n2:
        a_list[k] = r_list[j]
        k += 1
        j += 1


def merge_sort(a, l_index, r_index):
    if l_index < r_index:
        med_index = (l_index + r_index) // 2

        merge_sort(a, l_index, med_index)
        merge_sort(a, med_index+1, r_index)

        merge_list(a, l_index, med_index, r_index)

    return a


def merge_sort_runner(a):

    return merge_sort(a, 0, len(a)-1)


def binary_search_v(a, start, finish, v):
    diff = finish - start
    if diff == 0:
        return None

    diff = diff // 2
    if diff == 0:
        if a[start] == v:
            return start
        else:
            return None

    mediana = start + diff
    if a[mediana] == v:
        return mediana

    if a[mediana] < v:
        return binary_search_v(a, mediana + 1, finish, v)
    else:
        return binary_search_v(a, start, mediana, v)


def binary_search(a, v):
    return binary_search_v(a, 0, len(a), v)


def exact_sum(a, x):
    a = merge_sort(a, 0, len(a)-1)

    if a[0] > x:
        return False

    if (x / 2) > a[-1]:
        return False

    for i in range(len(a)-1):
        v = x - a[i]
        res = binary_search_v(a, i, len(a), v)

        if res:
            return [a[i], a[res]]

    return False


def merge_list_inversion_calc(a_list, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    l_list = [a_list[p+i] for i in range(n1)]
    r_list = [a_list[q+j+1] for j in range(n2)]

    i = 0
    j = 0
    k = p
    inversion = 0
    while i < n1 and j < n2:
        if l_list[i] <= r_list[j]:
            a_list[k] = l_list[i]
            i += 1
        else:
            a_list[k] = r_list[j]
            j += 1
            inversion += (n1 - i)
        k += 1

    while i < n1:
        a_list[k] = l_list[i]
        k += 1
        i += 1

    while j < n2:
        a_list[k] = r_list[j]
        k += 1
        j += 1

    return inversion


def merge_sort_inversions(a, l_index, r_index):
    inversion = 0
    if l_index < r_index:
        med_index = (l_index + r_index) // 2

        inversion += merge_sort_inversions(a, l_index, med_index)
        inversion += merge_sort_inversions(a, med_index+1, r_index)

        inversion += merge_list_inversion_calc(a, l_index, med_index, r_index)

    return inversion


def calc_inversions(a):

    return merge_sort_inversions(a, 0, len(a)-1)


if __name__ == "__main__":
#    a = [5, 2, 4, 6, 1, 3]
#    a = [31, 41, 59, 26, 41, 58]
#    a = [x for x in range(10)]
#    a = [2, 3, 8, 6, 1]
    a = [3, 2, 1, 0]
    print(a)
    res = merge_sort_runner(a)
    print(a)
    print(res)
