"""
문제에서 요구하는 것은 queue1과 queue2의 원소 합을 같게 만드는 것입니다.
처음 주어진 queue1의 합을 L, queue2의 합을 R이라고 했을 때,
L과 R을 같게 만들기 위해서는 다음과 같은 탐욕법을 사용하여 해결할 수 있습니다.

L > R이라면, queue1의 원소를 queue2로 넘겨줍니다.
L < R이라면, queue2의 원소를 queue1로 넘겨줍니다.
"""
from collections import deque


def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    count, max_count = 0, len(q1) * 3

    if s1 == s2:
        return 0
    elif (s1 + s2) % 2 == 1:  # 같아질 수 없음
        return -1

    while True:
        if s1 > s2:
            i = q1.popleft()
            q2.append(i)
            s1 -= i
            s2 += i
            count += 1
        elif s2 > s1:
            i = q2.popleft()
            q1.append(i)
            s2 -= i
            s1 += i
            count += 1
        else:
            break
        if count == max_count:
            return -1

    return count
