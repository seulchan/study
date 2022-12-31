# https://leetcode.com/problems/concatenation-of-array
# memory usage: 14.2 MB, time usage: 94 ms
from typing import Optional, List


def getConcatenation(nums: List[int]) -> List[int]:
    return nums * 2


if __name__ == "__main__":
    nums = [1, 3, 5]
    print(getConcatenation(nums))