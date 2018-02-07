
def find_max_crossing_subarray(a_list, low, mid, high):
    max_left = mid
    left_sum = a_list[max_left]
    sub_sum = 0
    for i in range(mid, low+1, -1):
        sub_sum += a_list[i]
        if sub_sum > left_sum:
            max_left, left_sum = i, sub_sum

    max_right = mid + 1
    right_sum = a_list[max_right]
    sub_sum = 0
    for i in range(mid+1, high+1):
        sub_sum += a_list[i]
        if sub_sum > right_sum:
            max_right, right_sum = i, sub_sum

    return [max_left, max_right, left_sum + right_sum]


def find_max_subarray(a_list, low, high):
    if low == high:
        return [low, high, a_list[low]]

    mid = (low + high)//2

    left_low, left_high, left_sum = find_max_subarray(a_list, low, mid)
    right_low, right_high, right_sum = find_max_subarray(a_list, mid+1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(a_list, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return [left_low, left_high, left_sum]
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return [right_low, right_high, right_sum]
    else:
        return [cross_low, cross_high, cross_sum]


def find_max_subarray_brute_force(a_list):
    max_sub_sum = a_list[0]
    max_left = 0
    max_right = 0
    for left_index in range(len(a_list)):
        sub_sum = a_list[left_index]
        if sub_sum > max_sub_sum:
            max_left, max_right, max_sub_sum = left_index, left_index, sub_sum

        for right_index in range(left_index+1, len(a_list), 1):
            sub_sum += a_list[right_index]
            if sub_sum > max_sub_sum:
                max_left, max_right, max_sub_sum = left_index, right_index, sub_sum

    return [max_left, max_right, max_sub_sum]


if __name__ == "__main__":
#    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    a = [-13, -3, -25, -20, -3, -16, -23, -18, -20, -7, -12, -5, -22, -15, -4, -7]

    print(a)
#    max_low, max_high, max_sub_sum = find_max_subarray(a, 0, len(a)-1)
    max_low, max_high, max_sub_sum = find_max_subarray_brute_force(a)

    print('max-low: {}\n max-high: {}\n max-sum: {}\n'.format(max_low, max_high, max_sub_sum))
