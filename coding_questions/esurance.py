
import collections


def calc_manipulations(a_str, b_str):
    a_dict = collections.defaultdict(int)

    for ch in a_str:
        a_dict[ch] += 1

    count = 0
    for ch in b_str:
        a_dict[ch] -= 1
        if a_dict[ch] < 0:
            count += 1

    if count > len(a_str) or count > len(b_str):
        return -1

    return count


def anagram_manipulations(a_list, b_list):
    res = []
    for i in range(len(a_list)):
        res.append(calc_manipulations(a_list[i], b_list[i]))

    return res


if __name__ == '__main__':
    a = ['a']
    b = ['bb']

    print(a)
    print(b)

    res = anagram_manipulations(a, b)

    print(res)
