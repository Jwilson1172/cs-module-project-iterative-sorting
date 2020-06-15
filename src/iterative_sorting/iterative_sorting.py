import time


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    count = 0
    A = arr

    # Traverse through all array elements
    for i in range(len(A)):
        count = count + 1
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            count = count + 1
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
    print("number of iter: {}".format(count))
    return A


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    count = 0
    n = len(arr)

    # loop through all elements
    for i in range(n - 1):
        count = count + 1
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            count = count + 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("number of iter: {}".format(count))
    return arr


"""
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    # Your code here

    return arr


if __name__ == "__main__":
    a = [1, 99, 2, 98, 3, 97, 4, 96, 5, 95, 6, 94, 7, 93, 8, 92, 9, 91, 10, 90]
    print("Passed array {}".format(a))
    st = time.time()
    print("Selection Sort Algo: {}".format(selection_sort(a)))
    stt = time.time()
    print("Ex-time: {}".format((stt - st)))
    st = time.time()
    print("Bubble Sort Algo: {}".format(bubble_sort(a)))
    stt = time.time()
    print("Ex-time: {}".format(stt - st))
