#!/usr/bin/env python

'''
Question: Given 3 sorted list, output the smallest 3 negative numbers
Anwser: The following solution can extend to more than 3 lists
'''

def process_3_lists(l0, l1, l2):
    res_list = []
    all_list = [l0, l1, l2] 

    # This is for some corner cases, if some lists are empty, make them non-empty
    for l in all_list:
        l.append(1)

    while True:
        res = sorted(all_list, key=lambda x: x[0])[0].pop(0)

        if res >= 0 or len(res_list) == 3:
            break;

        res_list.append(res)

    return res_list

if __name__ == '__main__':

    l0 = [-3, -2]
    l1 = [-3, -2]
    l2 = [-3, -2]
    print(process_3_lists(l0, l1, l2))

    l0 = [-3, +2]
    l1 = [-2, +2]
    l2 = [-1, +2]
    print(process_3_lists(l0, l1, l2))

    l0 = []
    l1 = []
    l2 = []
    print(process_3_lists(l0, l1, l2))

    l0 = [-3]
    l1 = [-1]
    l2 = []
    print(process_3_lists(l0, l1, l2))

    l0 = [-3]
    l1 = [2]
    l2 = []
    print(process_3_lists(l0, l1, l2))
