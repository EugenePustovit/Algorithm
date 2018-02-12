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

# import collections
#
# def subsequence(target_tag_list, tag_list):
#     tag_dict = collections.defaultdict(list)
#
#     for i in range(len(tag_list)):
#         tag_dict[tag_list[i]].append(i)
#
#     res = [0, len(tag_list)-1]
#     for tag in target_tag_list:
#         pass
#



if __name__ == "__main__":
#    a = 'democracy'
    a = 'awaglk'
    k = 4

    print('{} {}'.format(a, k))

    res = substring_list(a, k)

    print(res)
