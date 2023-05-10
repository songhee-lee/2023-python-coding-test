'''
n개의 여행지
1~n번까지의 번호로 구분
두 여행지 사이 연결하는 도로 존재 가능, 양방향 이동 가능
여행계획이 가능한지 여부 판별
가능하면 yes, 불가능하면 no

'''

def find_root(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

# 두 집합을 합치기
def union_sets(parent, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

# 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = list(range(n+1))

# Union 연산을 각각 수행
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        if data[j-1] == 1: # 연결된 경우 합집합(Union) 연산 수행
            union_sets(parent, i, j)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
is_possible = all(find_root(parent, plan[i]) == find_root(parent, plan[i+1]) for i in range(m-1))

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if is_possible:
    print("YES")
else:
    print("NO")
