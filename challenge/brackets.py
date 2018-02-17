
def is_balanced(s):
    if len(s) % 2 != 0:
        return False

    BR = {'(': ')', '[': ']', '{': '}'}

    if not BR.get(s[0]):
        return False

    br_list = [s[0]]
    for i in range(1, len(s)):
        if BR.get(s[i]):
            br_list.append(s[i])
        else:
            if not br_list:
                return False
            br = br_list.pop()
            if BR[br] != s[i]:
                return False

    if br_list:
        return False

    return True


def check_balance(a_list):
    for s in a_list:
        print(is_balanced(s))


if __name__ == '__main__':
    a = ['{[()]}', '{[(])}', '{{[[(())]]}}']

    print(a)

    check_balance(a)
