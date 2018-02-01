import collections


def is_valid_str(str, num):
    res_dict = collections.defaultdict(int)

    for ch in str:
        res_dict[ch] += 1

    if len(res_dict) == num - 1:
        return True

    return False


def subStringsLessKDist(inputString, num):
    res = []

    str_len = len(inputString)

    if num > str_len:
        return []

    for i in range(str_len - num):
        sub_string = inputString[i:i + num]

        if is_valid_str(sub_string, num):
            res.append(sub_string)

    return res


if __name__ == "__main__":
    a = 'democracy'
    print(a)
    res = subStringsLessKDist(a, 5)
    print(res)