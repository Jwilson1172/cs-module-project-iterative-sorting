import math


def linear_search(arr, target):
    """Searches for the target in the passed array will return either the index
    that that target is at in the list of it will return -1 if it is not found
    """
    # quick and dirty way of doing a linear search, using a list comprehesion
    # and a try/except block to catch the not found in array case by
    # chaching the index out of bounds execption that gets raised when the
    # target is not found.
    try:
        target_index = [x for x in range(len(arr)) if arr[x] == target]
        return target_index[0]
    except Exception:
        return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    n = len(arr)
    L = 0
    R = n - 1

    while L <= R:
        # find the mid point in the array
        mid = math.floor((L + R) / 2)
        # check if the target is on the left or right of the mid point
        # by making an ajustment to the mid points location by repeated iterations
        # when the target is found by halfing the trees it is returned
        if arr[mid] < target:
            L = mid + 1
        elif arr[mid] > target:
            R = mid - 1
        else:
            return mid
    # if the number is not found just return -1
    return -1


if __name__ == "__main__":
    a = [12, 10, 11, 15, 3, 99, 98, 97, 6]
    target = 99
    print(
        "the index of the target of {}, is: {} using the Linear Search function".format(
            target, linear_search(a, target)
        )
    )
    print(
        "the index of the target of {}, is: {} using the binary teach function".format(
            target, binary_search(a, target)
        )
    )
