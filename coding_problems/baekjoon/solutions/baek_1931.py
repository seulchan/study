# https://www.acmicpc.net/problem/1931
# memory usage: 57416 KB, time usage: 276 ms
import sys


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    meeting_list = [list(map(int, sys.stdin.readline().split())) for i in range(num)]
    meeting_list.sort(key=lambda x: (x[1], x[0]))
    picked_meeting = meeting_list[0]
    count = 1

    for meeting in meeting_list[1:]:
        if meeting[0] >= picked_meeting[1]:
            count += 1
            picked_meeting = meeting

    print(count)
