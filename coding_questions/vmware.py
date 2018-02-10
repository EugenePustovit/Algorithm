# perform operations without using eval()
#
# "2+3" = 5
# "7-2+5" = 10
# "8+17-11-2" = 12
# "13-2*3+3*11" = 40

import re


def sum_num_with_op(num_list, op_list):
    str_sum = num_list[0]
    for i in range(len(op_list)):
        if op_list[i] == '+':
            str_sum += num_list[i+1]
        elif op_list[i] == '-':
            str_sum -= num_list[i+1]
        else:
            print('oops')

    return str_sum


def calc_str(str):
    num_list = re.split(r'\+|-', str)
    op_list = re.findall(r'\+|-', str)
    num_list = list(map(int, num_list))
#    num_list = [int(i) for i in num_list]

    return sum_num_with_op(num_list, op_list)


def calc_str_m(str):
    num_m_list = str.split('*')

    num_list = re.split(r'\+|-', num_m_list[0])
    op_list = re.findall(r'\+|-', num_m_list[0])
    num_list = list(map(int, num_list))

    for i in range(1, len(num_m_list)):
        num_list_buff = re.split(r'\+|-', num_m_list[i])
        op_list.extend(re.findall(r'\+|-', num_m_list[i]))
        num_list_buff = list(map(int, num_list_buff))

        num_list_buff[0] = num_list.pop() * num_list_buff[0]
        num_list.extend(num_list_buff)

    return sum_num_with_op(num_list, op_list)


# def calc_str_optimal(str):
#     num_list = re.split(r'\+|-|\*', str)
#     op_list = re.findall(r'\+|-|\*', str)
#     num_list = list(map(int, num_list))
#
#     str_sum = num_list[0]
#     i = 0
#     mult = 0
#     mult_buff = 0
#     while i < len(op_list):
#         if i < len(op_list)-1 and op_list[i+1] == '*':
#             num_list[i+1] *= num_list[i+2]
#             mult += 1
#         else:
#             if op_list[i] == '*':
#                 str_sum *= num_list[i+1]
#             elif op_list[i] == '+':
#                 str_sum += num_list[i+1]
#             elif op_list[i] == '-':
#                 str_sum -= num_list[i+1]
#             else:
#                 print('oops')
#             i += (1 + mult)
#             mult = 0
#
#     return str_sum


if __name__ == "__main__":
#    str = '3-45-67-8+9+0+1+22'
    str = '13-2*3+3*11'
    res = calc_str_m(str)
    print(res)
