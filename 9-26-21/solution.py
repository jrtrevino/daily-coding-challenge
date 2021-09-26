# a brute force solution attempt
# Start at the index i of arr, calculate the required number n,
# so that arr[i] + n = k, then search arr for that number.
# Return true if two numbers add up to k, else false.
def brute_force(arr, k):
    arr_length = len(arr)
    add_to_k = False
    # O(n) for the for loop
    for index in range(arr_length):
        current_val = arr[index]
        needed_val = k - current_val
        # to avoid grabbing the same number we are currently on, check if our needed val's
        # index does not equal the current index. This prevents using the same number twice.
        # nested O(n) for in operator, and O(n) for index operator
        if needed_val in arr and arr.index(needed_val) != index:
            add_to_k = True
            break

    # total complexity -> O(n) * (O(n) + O(n)) = O(n^2)
    return add_to_k


# This function calculates the needed value, n, such that n + arr[i] = k.
# arr[i] is the current value in the arr. This implementation only requires looping
# through arr once, so total time complexity is O(n). This is marginally faster than the
# brute force implementation, which is O(n^2).
# This is done by adding n to a dictionary, and checking if arr[i] is in the dictionary.
# If arr[i] is in the dictionary, then some other number required arr[i] to add up to k.
def dict_implementation(arr, k):
    values_dict = {}
    add_to_k = False
    # O(n) -> For loop
    for number in arr:
        # calculate the value we need to add to k
        needed_val = k - number
        # check if our current number is in values_dict.
        # If it is, that means some other number required the current number to add to k
        # Otherwise, we can add the needed value into the values_dict.
        # O(1) -> lookup
        if number not in values_dict:
            values_dict[needed_val] = 'Added'
        # Number found, so we can break
        else:
            add_to_k = True
            break
    return add_to_k


def test_function():
    # brute_force Then dictionary implementation pairs
    print(
        "Testing arr (bf): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([5, 7, 3, 9], 16, brute_force([5, 7, 3, 9], 16)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([5, 7, 3, 9], 16, dict_implementation([5, 7, 3, 9], 16)))
    print("\n")

    print(
        "Testing arr (bf): [{}] with k={}. Expected result: False. Calculated Result: {}"
        .format([7, 21, 4, 0], 22, brute_force([7, 21, 4, 0], 22)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: False. Calculated Result: {}"
        .format([7, 21, 4, 0], 22, dict_implementation([7, 21, 4, 0], 22)))
    print("\n")

    print(
        "Testing arr (bf): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([0, 0, 5, 7], 0, brute_force([0, 0, 5, 7], 0)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([0, 0, 5, 7], 0, dict_implementation([0, 0, 5, 7], 0)))
    print("\n")

    print(
        "Testing arr (bf): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([9, 18, 27, 36], 45, brute_force([9, 18, 27, 36], 45)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([9, 18, 27, 36], 45, dict_implementation([9, 18, 27, 36], 45)))
    print("\n")

    print(
        "Testing arr (bf): [{}] with k={}. Expected result: False. Calculated Result: {}"
        .format([9, 1, 5, 2], 18, brute_force([9, 1, 5, 2], 18)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: False. Calculated Result: {}"
        .format([9, 1, 5, 2], 18, dict_implementation([9, 1, 5, 2], 18)))
    print("\n")

    print(
        "Testing arr (bf): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([0, 0, 0, 1], 1, brute_force([0, 0, 0, 1], 1)))
    print(
        "Testing arr (dict): [{}] with k={}. Expected result: True. Calculated Result: {}"
        .format([0, 0, 0, 1], 1, dict_implementation([0, 0, 0, 1], 1)))
    print("\n")


test_function()
