# Problem #1 - Solution

def check_string(str):
    str_set = set(list(str))

    if len(str_set) == len(str) - 1:
        return True

    return False


def substring_list(input_str, k):
    str_len = len(input_str)

    if k > str_len:
        return []

    res = []
    for i in range(str_len - (k-1)):
        sub_str = input_str[i:i+k]

        if check_string(sub_str):
            res.append(sub_str)

    return res


# ----------------------------------------------
# Problem #2 - Solution


import collections


def subsequence(target_tag_list, tag_list):

    if len(tag_list) < len(target_tag_list):
        return [0]

    target_tag_dict = collections.defaultdict(int)
    tag_dict = collections.defaultdict(int)

    for target_tag in target_tag_list:
        target_tag_dict[target_tag] += 1

    start = 0
    tag_count = 0
    start_index = -1
    min_len = len(tag_list)
    for i in range(len(tag_list)):
        tag_dict[tag_list[i]] += 1

        if target_tag_dict[tag_list[i]] != 0\
                and tag_dict[tag_list[i]] <= target_tag_dict[tag_list[i]]:
            tag_count += 1

        if tag_count == len(target_tag_list):

            while tag_dict[tag_list[start]] > target_tag_dict[tag_list[start]]\
                    or target_tag_dict[tag_list[start]] == 0:

                if tag_dict[tag_list[start]] > target_tag_dict[tag_list[start]]:
                    tag_dict[tag_list[start]] -= 1

                start += 1

            len_win = i - start + 1
            if min_len > len_win:
                min_len = len_win
                start_index = start

    if start_index == -1:
        return [0]

    return [start_index, start_index+min_len]


# ------------------------------------
# Given an image, represented by a two dimensional array of integers,
# write a function that rotates the image 90 degrees clockwise.


def rotate_90(arr):
    res = []

    # for i in range(len(arr[0])):
    #     res[i] = []

    for row in range(1, len(arr) + 1):
        for col in range(len(arr[0])):
            if res[col] is not list:
                res[col] = []
            res[col].append(arr[-1 * row][col])

    return res


if __name__ == "__main__":
#    a = 'democracy'
#     a = 'awaglk'
#     k = 4
#
#     print('{} {}'.format(a, k))
#
#     res = substring_list(a, k)
#
#     print(res)

    tags = ['made', 'weather', 'forecast', 'says', 'that', 'made', 'rain', 'in', 'spain', 'stays']
    target = ['made', 'in', 'spain']

    print(tags)
    print(target)

    res = subsequence(target, tags)

    print(res)
