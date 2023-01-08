# https://leetcode.com/problems/design-browser-history/
# memory usage: 13.9 MB, time usage: 28 ms


def tribonacci(n: int) -> int:
    dp = [0, 1, 1]

    if (n == 0 or n == 1 or n == 2):
        return dp[n]

    for i in range(3, n + 1):
        dp.append(sum(dp[(i - 3):]))

    return dp[-1]


# Space Optimisation : Dynamic Programming
def tribonacci_space(n: int) -> int:
    if n < 3:
        return 1 if n else 0

    x, y, z = 0, 1, 1
    for _ in range(n - 2):
        x, y, z = y, z, x + y + z
    return z


# Performance Optimisation : Dynamic Programming
class Tri:
    def __init__(self):
        n = 38
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]

class Solution:
    t = Tri()

    def tribonacci(self, n: int) -> int:
        return self.t.nums[n]
