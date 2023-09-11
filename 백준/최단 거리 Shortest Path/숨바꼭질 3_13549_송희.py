"""
수빈이는 점 N, 동생은 점 K에 위치해 있다.
수빈이는 1초 후 N-1 또는 N+1로 거리 1을 이동하거나, 0초후 2*N으로 순간 이동할 수 있다.
수빈이가 동생을 찾을 수 있는 가장 빠른 시간 구하기

0 <= N, K <= 100,000
"""

from collections import deque

N, K = map(int, input().split())
q = deque([N])
# time[k] : k점으로 이동하는데 걸리는 최소 시간
time = [100_000] * 100_001
time[N] = 0
while q :
    x = q.popleft()

    # -1 이동
    if x-1 >= 0 and time[x-1] > time[x]+1 :
        time[x-1] = time[x]+1
        q.append(x-1)
    # +1 이동
    if x+1 <= 100_000 and time[x+1] > time[x]+1 :
        time[x+1] = time[x]+1
        q.append(x+1)
    # 순간 이동
    if 2*x <= 100_000 and time[2*x] > time[x] :
        time[2*x] = time[x]
        q.append(2*x)

print(time[K])