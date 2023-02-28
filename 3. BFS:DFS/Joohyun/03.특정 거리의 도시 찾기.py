from collections import deque
# 입력
# N : 도시 개수
# M : 도로 개수
# K : 거리 정보
# X : 출발 도시 번호
N, M, K, X = map(int,input().split())

# map(도시-도로 정보) 초기화 및 update
map=[[] for _ in range(N+1)]
for m in range(M):
    i,j = input().split()
    map[int(i)].append(int(j))

# 출발 도시로부터 각 도시까지의 최단거리
distances = {}
for n in range(N):
    distances[n+1]=-1   # 최단거리 초기화


def bfs(map,distances,X,K,step):
    queue = deque([(X,step)])       # X : 출발 도시, step : 이동 거리
    
    while queue:
        v,step = queue.popleft()    # v : 출발 도시, step : 이동 거리

        # 최단거리 update
        if distances[v]== -1 : distances[v]=step

        # 현재 도시에서 갈 수 있는 도시, 다음 도시까지 이동 거리 update (queue에 삽입)
        for i in map[v]:
            queue.append((i,step+1))  # i : 현재 도시에서 갈 수 있는 도시
                                    # step+1 : 다음 도시까지 이동 거리
            
bfs(map,distances,X,K,0)

# 최단거리가 K와 동일한 도시 찾기
city = [] # 최단거리가 K와 같은 도시
for d in distances:
    if distances[d]==K : city.append(d)
print(*sorted(city), sep='\n') if city else print(-1)
