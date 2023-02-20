"""Psuedo Code
https://www.acmicpc.net/problem/15686

1. 도시 크기 N, 치킨집 개수 M, 도시정보 입력 받기
    - 0 빈칸, 1 집 2 치킨집
    - 1 <= 집 <= 2*N 
    - M <= 치킨집 <= 13
2. 각 집마다 가까운 순으로 치킨집 정렬
3. 치킨집 M개 고르기
4. 도시의 치킨거리 최솟값 출력

    * 치킨 거리 : 가장 가까운 치킨집과의 거리 |x - y|
    * 도시의 치킨 거리 : 모든 치킨 거리의 합
"""

from itertools import combinations

# 1. 입력 받기
N, M = map(int, input().split())

chicken, house = [], []    # 치킨집 위치, 집 위치
for i in range(1, N+1):
    for j, x in enumerate(list(map(int, input().split()))) :
        if x == 2 :
            chicken.append((i, j+1))
        elif x == 1 :
            house.append((i, j+1))

# 2. 각 집마다 가까운 순으로 치킨집 정렬
c_distance = {}   # dict[집 위치] = [ (치킨집 위치, 거리), ..]
for x_h, y_h in house:
    distance = [ ( c[0], c[1], abs(x_h - c[0]) + abs(y_h - c[1])) for c in chicken]
    distance = sorted(distance, key=lambda x: x[2])
    c_distance[(x_h, y_h)] = distance

# 3. 치킨집 M개 고르기
result = 1e9
for c in combinations(chicken, M) :
    city_distance = 0

    # 각 집마다 가장 가까운 치킨집 고르기
    for x_h, x_y in house:
        
        for x_c, y_c, d in c_distance[(x_h, y_h)]:
            if (x_c, y_c) in c:
                city_distance += d
                break
    
    result = min(result, city_distance)

print(result)