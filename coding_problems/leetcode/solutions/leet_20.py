# https://leetcode.com/problems/valid-parentheses/
# memory usage: 13.9 MB, time usage: 37 ms


def is_valid(s: str) -> bool:
    symbol_map = {')': '(', ']': '[', '}': '{'}
    open_parentheses = []

    for symbol in list(s):
        if symbol in ['(', '{', '[']:
            open_parentheses.append(symbol)
            continue

        if len(open_parentheses) == 0 or open_parentheses.pop() != symbol_map[symbol]:
            return False

    if len(open_parentheses) > 0:
        return False

    return True


def isValid2(s: str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack


if __name__ == "__main__":
    s = "()[]{}"
    print(is_valid(s))

    s = "([]{}"
    print(is_valid(s))
