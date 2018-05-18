# -*- coding:utf-8 -*-

"""

@file: find_greater_number.py
@time: 2018/4/14

"""

def construct_number_from_intlist(intlist):
    # to str list
    strlist = [str(i) for i in intlist]
    return int(''.join(strlist))


def find_greater_idx(first_num, aoreder_cnum_list):
    idx = aoreder_cnum_list.index(first_num)
    while idx < len(aoreder_cnum_list):
        if aoreder_cnum_list[idx] > first_num:
            # idx found
            return idx

        idx += 1


def greater_finder(numbers_str, RIGHT = 2):
    LENGTH = len(numbers_str)

    while RIGHT <= LENGTH:
        # TODO
        # find geater number among RIGHT numbers
        current_num_str = numbers_str[-RIGHT:]
        current_num = int(current_num_str)
        # list
        cnum_list = [int(s) for s in current_num_str]

        # descending order
        dorder_cnum_list = cnum_list.copy()
        dorder_cnum_list.sort(reverse=True)
        dorder_cnum = construct_number_from_intlist(dorder_cnum_list)

        if dorder_cnum == current_num:
            # RIGHT + 1
            RIGHT += 1
            return greater_finder(numbers_str, RIGHT)

        # dorder_cnum != current_num

        # ascending order
        aoreder_cnum_list = cnum_list.copy()
        aoreder_cnum_list.sort()
        # first number of current num
        first_num = int(current_num_str[0])
        greater_cnum_idx = find_greater_idx(first_num, aoreder_cnum_list)
        n_h = aoreder_cnum_list[greater_cnum_idx]
        del aoreder_cnum_list[greater_cnum_idx]
        aoreder_cnum_list.insert(0, n_h)

        if RIGHT == LENGTH:
            return ''.join([str(i) for i in aoreder_cnum_list])
        else:

            left_numbers = numbers_str[:(LENGTH - RIGHT)]
            right_numbers = ''.join([str(i) for i in aoreder_cnum_list])
            return left_numbers + right_numbers

    # not found
    return -1

def next_bigger(n):
    numbers_str = str(n)
    result = greater_finder(numbers_str)
    return int(result)

# if __name__ == '__main__':
    # result = greater_finder(numbers_str)
    # print(result)
