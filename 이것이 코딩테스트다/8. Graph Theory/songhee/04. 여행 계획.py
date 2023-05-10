
# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
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
parent = [i for i in range(N+1)]    # 부모 테이블

# 연결된 여행지 정보
for i in range(N):
    link = list(map(int, input().split()))  # 연결 정보
    for j in range(N):
        if link[j] == 1:                    # 연결된 경우
            union_parent(parent, i+1, j+1)  # 합치기

places = list(map(int, input().split()))    # 여행 계획

# 모든 여행지의 부모가 같으면 여행 가능
p = find_parent(parent, places[0])          
answer = "YES"
for x in places[1:]:
    if p != find_parent(parent, x):
        answer = "NO"
        break

print(answer)