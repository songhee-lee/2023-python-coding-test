import sys
input = sys.stdin.readline

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
N = int(input())

x = []  # x 좌표
y = []  # y 좌표
z = []  # z 좌표
for i in range(1, N+1):
    coor = list(map(int, input().split()))
    x.append((coor[0], i))
    y.append((coor[1], i))
    z.append((coor[2], i))

x.sort()
y.sort()
z.sort()

parent = [i for i in range(N+1)]    # 부모 테이블
edges = []       # 간선 리스트
answer = 0       # 터널 연결 비용

# 각 좌표별 N-1 개의 간선 추가
for i in range(N-1):
    edges.append((x[i+1][0] - x[i][0], x[i+1][1], x[i][1]))
    edges.append((y[i+1][0] - y[i][0], y[i+1][1], y[i][1]))
    edges.append((z[i+1][0] - z[i][0], z[i+1][1], z[i][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 행성 터널이 없는 경우에만 연결
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)