import random
from typing import List
# https://leetcode.com/problems/binary-search/


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

if __name__ == "__main__":
    target = 9
    data_list = random.sample(range(20), 10)
    data_list = sorted(data_list)
    print("data:", data_list)
    print("target:", target)
    print("result:", binary_search(data_list, target))
