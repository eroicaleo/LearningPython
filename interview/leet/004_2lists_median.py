#!/usr/bin/env python

def process_lists(l1, l2, k):

    # k is a index in range(0, k)
    l1_lo, l1_hi, l2_lo, l2_hi = 0, len(l1)-1, 0, len(l2)-1

    while True:

        # break condition 2, lo > hi
        if l1_hi < l1_lo:
            print('crossing l1_lo: %d, l1_hi: %d.' % (l1_lo, l1_hi))
            return l2[l2_lo+k]
        if l2_hi < l2_lo:
            print('crossing l2_lo: %d, l2_hi: %d.' % (l2_lo, l2_hi))
            return l1[l1_lo+k]

        print('#' * 80)
        print("Initial: l1_lo: %d, l1_hi: %d, l2_lo: %d, l2_hi: %d" % (l1_lo, l1_hi, l2_lo, l2_hi))
        print('looking for No. %d element in %s and %s' % (k, l1[l1_lo:l1_hi+1], l2[l2_lo:l2_hi+1]))

        # After these two steps, l1 and l2 are at most length k-1
        # Index k more close to 0 or len(l1) + len(l2) ?
        j = (l1_hi-l1_lo+1) + (l2_hi-l2_lo+1) - 1 - k
        if k <= j:
            l1_hi = min(l1_hi, l1_lo+k)
            l2_hi = min(l2_hi, l2_lo+k)
        else:
            l1_lo = max(l1_lo, l1_hi-j)
            l2_lo = max(l2_lo, l2_hi-j)

        print("Reduce length: l1_lo: %d, l1_hi: %d, l2_lo: %d, l2_hi: %d" % (l1_lo, l1_hi, l2_lo, l2_hi))
        print('looking for the element in %s and %s' % (l1[l1_lo:l1_hi+1], l2[l2_lo:l2_hi+1]))

        # temination condition:
        if k == 0:
            print('k = %d' % k)
            return min(l1[l1_lo], l2[l2_lo])
        if j == 0:
            print('j = %d' % j)
            return max(l1[l1_hi], l2[l2_hi])
        
        if k <= j:
            # Remove k/2 element 
            move = int((k-1)/2)
            l1_mi, l2_mi = [l + move for l in [l1_lo, l2_lo]]
            # they cann't be bigger than l?_hi
            l1_mi, l2_mi = min(l1_mi, l1_hi), min(l2_mi, l2_hi)
            print("l1[l1_mi] : %d, l2[l2_mi] : %d" % (l1[l1_mi], l2[l2_mi]))
            if l1[l1_mi] <= l2[l2_mi]:
                real_move = min(l1_hi+1, l1_lo+move+1) - l1_lo
                l1_lo += real_move
            else:
                real_move = min(l2_hi+1, l2_lo+move+1) - l2_lo
                l2_lo += real_move
            k -= real_move
        else:
            # Remove j/2 element
            move = int((j-1)/2)
            l1_mi, l2_mi = [l - move for l in [l1_hi, l2_hi]]
            # they cann't be smaller than l?_lo
            l1_mi, l2_mi = max(l1_mi, l1_lo), max(l2_mi, l2_lo)
            print("l1[l1_mi] : %d, l2[l2_mi] : %d" % (l1[l1_mi], l2[l2_mi]))
            if l1[l1_mi] >= l2[l2_mi]:
                real_move = l1_hi - max(l1_lo-1, l1_hi-move-1)
                l1_hi -= real_move
            else:
                real_move = l2_hi - max(l2_lo-1, l2_hi-move-1)
                l2_hi -= real_move
            k = (l1_hi-l1_lo+1) + (l2_hi-l2_lo+1) - 1 - (j-real_move)

        print("Remove k/2 elements: l1_lo: %d, l1_hi: %d, l2_lo: %d, l2_hi: %d" % (l1_lo, l1_hi, l2_lo, l2_hi))
        print('looking for No. %d element in %s and %s' % (k, l1[l1_lo:l1_hi+1], l2[l2_lo:l2_hi+1]))

        # break condition 2, lo > hi
        if l1_hi < l1_lo:
            print('crossing l1_lo: %d, l1_hi: %d.' % (l1_lo, l1_hi))
            return l2[l2_lo+k]
        if l2_hi < l2_lo:
            print('crossing l2_lo: %d, l2_hi: %d.' % (l2_lo, l2_hi))
            return l1[l1_lo+k]

if __name__ == '__main__':
    # l1 = [1, 2, 3]
    # l2 = [4, 5, 6]
    # for i in range(0, len(l1+l2)):
    #     print('## Iteration i = %d' % i)
    #     print(process_lists(l1, l2, i))

    # l1 = list(range(1, 9, 2))
    # l2 = list(range(2, 10, 2))
    # for i in range(len(l1+l2)):
    #     print('## Iteration i = %d' % i)
    #     print(process_lists(l1, l2, i))

    # l1 = [7]
    # l2 = list(range(0, 7)) + list(range(8, 16))
    # for i in range(len(l1+l2)):
    #     print('## Iteration i = %d' % i)
    #     print(process_lists(l1, l2, i))

    l1 = [1]
    l2 = [2, 3, 4, 5, 6, 7]
    l = (len(l1) + len(l2)) // 2
    print(process_lists(l1, l2, l))

    l1 = [2,3,5,6,8,9]
    l2 = [1,4,7]
    l = (len(l1) + len(l2)) // 2
    print(process_lists(l1, l2, l))
