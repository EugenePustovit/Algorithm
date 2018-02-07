# 1. Distinct chars in String
#
# given a String.
# Return True if all chars in string distinct
# Return False if at least one char repeated more than once
#
# example:
#
# str = 'abcd'
# res = check_string(str)
# print(res)
#
# str = 'abacd'
# res = check_string(str)
# print(res)
#
# output:
# True
# False


import collections


def check_string(str):
    char_dict = collections.defaultdict(int)

    for ch in str:
        char_dict[ch] += 1
        if char_dict[ch] > 1:
            return False

    return True


def check_string_(str):
    str_set = set(list(str))
    if len(str_set) != len(str):
        return False

    return True


# 2. Happy number
#
# given a list of integers. Check each value for happiness.
#
# Happy number verification:
#
# The number is Happy if the sum of squares of it's digits equal number itself or 1
# If in any iteration we get a sum different from initial number and 1 but which we already had in one of the previos
# iterations then this number isn't happy
#
# example:
#
# num = 89
#           8^2 + 9^2 = 64 + 81 = 145
#     1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
#           4^2 + 2^2 = 16 + 4 = 20
#           2^2 + 0^2 = 4 + 0 = 4
#                 4^2 = 16
#           1^2 + 6^2 = 1 + 36 = 37
#           3^2 + 7^2 = 9 + 49 = 58
#           5^2 + 8^2 = 25 + 64 = 89 == num   <= the sum is equal to initial number, that's mean it's a Happy number
#
#
# num = 123
#     1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
#           1^2 + 4^2 = 1 + 16 = 17
#           1^2 + 7^2 = 1 + 49 = 50
#           5^2 + 0^2 = 25 + 0 = 25
#           2^2 + 5^2 = 4 + 25 = 29
#           2^2 + 9^2 = 4 + 81 = 85
#           8^2 + 5^2 = 64 + 25 = 89    <=!
#           8^2 + 9^2 = 64 + 81 = 145
#     1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
#           4^2 + 2^2 = 16 + 4 = 20
#           2^2 + 0^2 = 4 + 0 = 4
#                 4^2 = 16
#           1^2 + 6^2 = 1 + 36 = 37
#           3^2 + 7^2 = 9 + 49 = 58
#           5^2 + 8^2 = 25 + 64 = 89    <= these sums are the same, thats mean that it's not a Happy number
#
#
# The method should print number: True[or False] for each number in the provided list
# example:
#
# num_list = [123, 89]
# find_happiness(num_list)
#
# output:
# 123: False
# 89: True


def split_num_to_digits(num):
    return list(map(int, list(str(num))))


def happy_num(num_digit_list, num, sum_dict):
    sum = 0
    for num_digit in num_digit_list:
        sum += pow(num_digit, 2)

    if sum_dict.get(str(sum)):
        print('{}: False'.format(num))
        return
    else:
        sum_dict[str(sum)] = 1

    if sum == num or sum == 1:
        print('{}: True'.format(num))
        return

    num_digit_list = split_num_to_digits(sum)
    happy_num(num_digit_list, num, sum_dict)


def find_happiness(num_list):

    for num in num_list:
        sum_dict = {}
        num_digit_list = split_num_to_digits(num)
        happy_num(num_digit_list, num, sum_dict)


if __name__ == "__main__":
    a = 'abcd'
    print(a)
    res = check_string_(a)
    print(res)

    a = 'aa'
    print(a)
    res = check_string_(a)
    print(res)

    # a = [89, 123]
    # find_happiness(a)
