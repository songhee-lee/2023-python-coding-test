import heapq

"""
유니온 파인드
"""
# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())
# 마을 간 도로 입력 받기
q = []  # (비용, 마을1, 마을2)
for _ in range(M):
    x, y, z = map(int, input().split())
    heapq.heappush(q, (z, x, y))    

# 비용이 적은 도로부터 하나씩 추가하기
parent = [i for i in range(N)]  # 부모 테이블
answer = 0
while q:
    cost, a, b = heapq.heappop(q)
    # 길이 없는 경우 포함해야 한다.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    # 길이 이미 있는 경우 절약 가능!
    else:
        answer += cost

print(answer)
