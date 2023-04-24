from collections import deque

for testcase in range(int(input())):
    n=int(input())
    indegree = [0]*(n+1)
    graph=[[False]*(n+1) for i in range(n+1)]

    data=list(map(int,input().split()))

    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]]=True
            indegree[data[j]]+=1

    m=int(input())
    for i in range(m):
        a,b=map(int,input().split())

        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1
    
    result=[]
    q=deque()

    for i in range(1,n+1):
        if not indegree[i]: q.append(i)
    
    certain=True
    cycle=False

    for i in range(n):
        if not q:
            cycle=True
            break
        if len(q)>=2:
            certain=False
            break
        
        now=q.popleft()
        result.append(now)
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
    
    if cycle: print("IMPOSSIBLE")
    elif not certain: print("?")
    else: print(*result)