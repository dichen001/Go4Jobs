"""
the maximum subarray problem is the task of finding the
contiguous subarray within a one-dimensional array of numbers which has the largest sum.
"""


def max_subarray(A):
    """
    Kadane's algorithm
    :param A:
    :return:
    """
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far 