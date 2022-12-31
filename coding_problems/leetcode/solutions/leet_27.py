# https://leetcode.com/problems/remove-element/
# memory usage: 13.8 MB, time usage: 28 ms
from typing import Optional, List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for num in nums:
        if num != val:
            nums[i] = num
            i += 1
    return i


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3

    print(removeElement(nums, val))
    print(nums)