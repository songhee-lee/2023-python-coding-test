def find_parent(parent,a):
    if a!=parent[a]:
        parent[a]=find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:parent[b]=a
    else:parent[a]=b

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

edges=[]
for _ in range(m):
    x,y,z=map(int,input().split())
    edges.append((z,x,y))

edges.sort()
result,total=0,0    # 최종비용, 전체가로등비용

for e in edges:
    cost,x,y=e
    total+=cost

    if find_parent(parent,x)!=find_parent(parent,y):
        union_parent(parent,x,y)
        result+=cost

print(total-result)