# Returns the smallest positive integer missing from the array;

def smallest_positive_int(arr):
    seen_set = set()
    need_set = set()
    for number in arr:
        if number <= 0:
            continue
        seen_set.add(number)
        if number in need_set:
            need_set.remove(number)
        for i in range(1, number):
            if i not in seen_set:
                need_set.add(i)
    # two cases if need set is empty:
    #   1. All numbers were negative, so return 1
    #   2. The needed number is greater than the last seen number
    #      2a. In this case, return (last seen number + 1)
    if len(need_set) > 0:
        return list(need_set)[0]
    else:
        if (len(seen_set) > 0):
            return list(seen_set)[-1] + 1
        return 1


def tests():
    assert smallest_positive_int([2, 3, 4]) == 1
    assert smallest_positive_int([-1, -2, -4, -3]) == 1
    assert smallest_positive_int([1, 2, 3, 4, 5, 6, 7, 9, 10]) == 8
    assert smallest_positive_int([6, 9, 1, 2, 3, 4, 5, 8]) == 7
    assert smallest_positive_int([121]) == 1
    assert smallest_positive_int(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 20


tests()
