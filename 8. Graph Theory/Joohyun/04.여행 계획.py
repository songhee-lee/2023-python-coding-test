"""
여행지 N개 : 1번 ~ N번 번호 부여
도로로 연결 = 양방향 이동 가능
여행 가능 여부 판별
>> 서로소 집합
"""
# n:여행지 수   m:여행계획에 속한 도시 수
n,m=map(int,input().split())
parent=[i for i in range(n+1)]    # 부모 노드 테이블

def find_parent(parent,a):
    if a!=parent[a]:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:parent[b]=a
    else:parent[a]=b

# 도로 정보
graph=[[] for _ in range(n+1)]
for a in range(1,n+1):
    data=[0]+list(map(int,input().split()))
    for b in range(1,n+1):
        if data[b]==1:  # 도시a,도시b 연결 
            if find_parent(parent,a)!=find_parent(parent,b):
                union_parent(parent,a,b)

travel=list(map(int,input().split()))  # 여행 계획에 포함된 여행지 번호들
root = find_parent(parent,travel[0])
for t in travel[1:]:
    if find_parent(parent,t)!=root:
        print('NO')
        exit(0)
print('YES')