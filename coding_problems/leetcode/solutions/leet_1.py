# https://leetcode.com/problems/two-sum/
# memory usage: 45.5 MB, time usage: 8 ms
from typing import Optional, List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for num in nums:
        start_index = nums.index(num)
        if target - num in nums[start_index + 1:]:
            return [start_index, nums.index(target - num, start_index + 1)]