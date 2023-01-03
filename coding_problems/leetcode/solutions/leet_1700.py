# https://leetcode.com/problems/design-linked-list/
# memory usage: 13.8 MB, time usage: 94 ms
from typing import List


def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    count = 0
    while students and sandwiches:
        if count >= len(students):
            return len(students)

        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0
        else:
            students.append(students.pop(0))
            count += 1

    return 0

