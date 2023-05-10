"""
탑승구:G개 번호 1번~G번
비행기:P개
i번째 비행기를 1번부터 g_i번째 탑승구 중 빈 곳 하나에 영구적으로 도킹
>> 도킹 가능한 비행기 최대 개수
"""

def find_parent(parent,a):
    if a!=parent[a]:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:parent[b]=a
    else:parent[a]=b

g = int(input())    # 탑승구 개수
p = int(input())    # 비행기 개수
parent=[i for i in range(g+1)]  # 부모노드테이블 초기화

result=0
for _ in range(p):
    data=find_parent(parent,int(input()))
    if data==0:break
    union_parent(parent,data,data-1)
    result+=1

print(result)