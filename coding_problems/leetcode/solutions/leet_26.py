# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# memory usage: 15.6 MB, time usage: 81 ms
from typing import Optional, List


def removeDuplicates(nums: List[int]) -> int:
    index = 0

    if len(nums) == 1:
        return 1

    nums[index] = nums[0]

    for i in range(len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]
    return index + 1


def removeDuplicatesV2(nums: List[int]) -> int:
    k = 0
    i = 0
    while i < len(nums):
        val = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == val:
            nums.remove(val)
            k += 1
        i += 1
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(removeDuplicatesV2(nums))
    print(nums)
