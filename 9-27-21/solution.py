# Return a new array where each index i contains the product of all
# integers in arr except arr[i].
# This solution will calcuate the product of all integers in the arr
# and divide the product by each number in array to gen. the new arr.
def solution_division(arr):
    # our return arr
    product_arr = []
    product = None
    if len(arr) == 1:
        return product_arr

    # loop through arr to get product -> O(n)
    for integer in arr:
        if product is None:
            product = integer
        else:
            product = product * integer

    # loop through arr to divide by int -> O(n)
    for integer in arr:
        product_arr.append(product / integer)

    # O(N) + O(N) = O(N)
    return product_arr

# test function for results


def test_function():
    # brute_force Then dictionary implementation pairs
    print(
        "Testing arr): [{}]. Expected result: [189, 135, 315, 105]. Calculated Result: {}"
        .format([5, 7, 3, 9], solution_division([5, 7, 3, 9])))
    print(
        "Testing arr): [{}]. Expected result: True. Calculated Result: {}"
        .format([12, 1, 5, 16], solution_division([12, 1, 5, 16])))
    print("\n")

    print(
        "Testing arr): [{}]. Expected result: True. Calculated Result: {}"
        .format([40, -1, 3, -8], solution_division([40, -1, 3, -8])))
    print(
        "Testing arr): [{}]. Expected result: True. Calculated Result: {}"
        .format([-20, 5], solution_division([-20, 5])))
    print("\n")

    print(
        "Testing arr): [{}]. Expected result: True. Calculated Result: {}"
        .format([10], solution_division([10])))
    print(
        "Testing arr): [{}]. Expected result: True. Calculated Result: {}"
        .format([12, 12, 12], solution_division([12, 12, 12])))
    print("\n")
