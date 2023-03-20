'''
가장 많은 것 출력
여러개면 작은 것 출력
'''

from sys import stdin
input = stdin.readline


def solve():
    di = dict()

    for _ in range(int(input())):
        num = int(input())

        if num not in di:
            di[num] = 1
        else:
            di[num] += 1

    maxValue = max(di.values())
    for key in sorted(di.keys()):
        if di[key] == maxValue:
            return key


print(solve())
