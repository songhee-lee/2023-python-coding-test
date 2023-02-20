'''
[조건]
1. 점검 시간은 '1시간'으로 제한
2. 레스토랑의 정북 방향 지점 : 0
3. 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타낸다.
4. 친구들은 출발 지점부터 시계 or 반시계 방향으로 외벽을 따라서만 이동

[제한]
- 1 <= n <= 200 (n은 외벽의 둘레)
- 1 <= week <= 15 (오름차순 정렬되어 주어짐, 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 ❌)
- 1 <= dist <= 8

Flow✅
1. 어느 취약지점부터 점검할지, 취약지점의 시작지점을 설정한다.
2. dist 배열(각 친구가 이동할 수 있는 거리들)의 순열을 구해서, 하나씩 순회한다.
3. (2)에서 구한 순열의 원소를 순회하면서 시작지점을 업데이트한다.(시작지점 = 시작지점 + 현재 순열의 원소)
4. 현재 시작지점과 외벽의 끝 지점의 크기를 살핀다.
    4.1 만약, 현재 시작지점이 외벽의 끝 지점보다 크거나 같다면, 모든 외벽을 점검한 것이므로 필요한 친구 수를 저장한다.
    4.2 만약, 그렇지 않다면, 시작지점을 "남은 외벽 취약 지점들 중 시작 지점보다 크고, 그 중에서 가장 작은 곳"으로 업데이트한다.
5. 모든 취약지점을 시작 지점으로 설정해서 순회할 때 까지 (1)로 돌아가 반복한다.
'''
from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak) 
    weak_circle = weak + [w + n for w in weak] # 원형 레스토랑이므로 
    min_friend = len(dist) + 1 # 투입할 최소 친구 수
    
    for i, start in enumerate(weak): # 시작 지점 설정
        for friends in permutations(dist): # dist 순열 순회
            friend_count = 1 
            pos = start # pos : 시작 지점
            
            for friend in friends: # 각 순열의 원소를 순회
                pos += friend # 시작 지점 업데이트 ex) pos : 1, friend : 1 => pos = 2(= 1에서 2까지는 살펴보았다는 의미)
                if pos < weak_circle[i + weak_len - 1]: # 만약, 취약 지점들의 마지막 지점보다 작다면(= 모든 취약 지점을 점검하지 못했을 경우)
                    friend_count += 1 # 친구 한명 더 투입
                    pos = [w for w in weak_circle[i + 1:i + weak_len] if w > pos][0] # 시작 지점을 남은 외벽 취약 지점들 중 시작 지점보다 크고, 그 중에서 가장 작은 곳으로 업데이트
                else: # 모든 취약 지점을 점검했을 경우
                    min_friend = min(min_friend, friend_count) # 투입할 최소 친구 수 업데이트
                    break
    return min_friend if min_friend != len(dist) + 1 else -1 # 만약, 친구들을 모두 투입했는데도 점검 할 수 없으면 return -1