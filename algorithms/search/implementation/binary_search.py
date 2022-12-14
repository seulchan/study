import random
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle

    return -1


# low = 1, high = 100
# Binary search on some range of values
def binary_search_on_range(low, high):
    while low <= high:
        middle = (low + high) // 2

        if is_correct(middle) > 0:
            high = middle - 1
        elif is_correct(middle) < 0:
            low = middle + 1
        else:
            return middle
    return -1


# Return 1 if n is too big, -1 if too small, 0 if correct
def is_correct(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0


if __name__ == "__main__":
    target = 9
    data_list = random.sample(range(20), 10)
    data_list = sorted(data_list)
    print("data:", data_list)
    print("target:", target)
    print("result:", binary_search(data_list, target))
