"""
집:N개  길:M개(유지비)

마을 분리 계획
분리된 마을 안에는 집들이 서로 연결되도록
>> 신장트리
"""

n,m = map(int,input().split())  # n:집개수  m:길개수
routes=[]
parent=[i for i in range(n+1)] # 부모 노드 테이블 초기화

def find_parent(parent,a):
    if a!=parent[a]:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:parent[b]=a
    else:parent[a]=b

# 길 정보
for _ in range(m):
    a,b,c=map(int,input().split())  # a집-b집 : 유지비c
    routes.append((c,a,b))

routes.sort(reverse=True)   # high_cost ~ low_cost
result, last = 0, 0  # 최종 비용, 가장 비용이 큰 간선

while routes:
    c,a,b = routes.pop()    # lowest cost

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=c
        last = c

print(result-last)




