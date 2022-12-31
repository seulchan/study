# https://leetcode.com/problems/baseball-game/
# memory usage: 14 MB, time usage: 43 ms
from typing import Optional, List


def calPoints(operations: List[str]) -> int:
    scores = []
    for op in operations:
        if op not in ['+', 'C', 'D']:
            scores.append(int(op))
        elif op == '+':
            scores.append(scores[-1] + scores[-2])
        elif op == 'C':
            scores.pop()
        elif op == 'D':
            scores.append(scores[-1] * 2)
    return sum(scores)


if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    print(calPoints(ops))