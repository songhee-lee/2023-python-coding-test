'''
다리 건설 비용 주어짐.
최소 비용으로 모든 섬이 통행 가능하도록 만들기 (최소 비용 return)

크루스칼 알고리즘
: 간선을 거리가 짧은 순서대로 그래프에 포함시키기
'''
#부모 노드 찾기
def getParent(parent, x) :
    if parent[x] == x: 
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 부모 노드 합치기
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    
    if a < b: 
        parent[b] = a
    else :
        parent[a] = b
        
# 같은 부모인지 확인
def findParent(parent, a , b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b: 
        return 1
    return 0
        
def solution(n, costs):
    answer = 0
    edge = len(costs)
    #모든 간선 정보를 오름차순으로 정렬
    costs.sort(key = lambda x:x[2])
    
    cycle = [i for i in range(n)]
    #print(cycle)
    #사이클이 형성하는 경우 간선 포함하지 않기 (Union-Find)
    #그래프 포함 (최소비용신장트리)
    for i in range(edge):
        if findParent(cycle, costs[i][0], costs[i][1])==0:
            answer += costs[i][2]
            unionParent(cycle, costs[i][0], costs[i][1])
    
    
    
    
    return answer