'''

[설명]
- 1번부터 M번까지 번호가 매겨져 있는 M개의 1인승 놀이기구가 있다. 
- 모든 놀이기구는 운행 시간이 정해져 있다.
- 놀이 기구가 비어 있으면 현재 줄에서 가장 앞에 서 있는 아이가 빈 놀이기구에 탑승한다.
- 만약, 여러 개의 놀이기구가 동시에 비어 있으면, 더 작은 번호가 적혀 있는 놀이기구를 먼저 탑승한다.
- 초기에 놀이기구가 모두 비어 있는 상태에서 첫 번째 아이가 놀이기구에 탑승한다고 할 때,
    줄의 마지막 아이가 타게 되는 놀이기구의 번호를 구하라

[아이디어]
- 

-> 몬말이야... 이해 안 됨..
-> ✅ 다시 풀기
'''

import sys
from heapq import heappush, heappop

def binary_search():
    l, r = 0, 60_000_000_000
    t = 0
    
    while l <= r:
        mid = l + (r - l) // 2
        cnt = m

        for i in range(m):
            cnt += mid // rides[i]
            
        if cnt >= n:
            t = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return t

n, m = map(int, sys.stdin.readline().split())

rides = list(map(int, sys.stdin.readline().split()))

if n < m:
    print(n)
else:
    t = binary_search()
    cnt = m
    
    for i in range(m):
        cnt += (t - 1) // rides[i]
    
    for i in range(m):
        if t % rides[i] == 0:
            cnt += 1
        
        if cnt == n:
            print(i + 1)
            break
    
    