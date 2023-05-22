from collections import deque

#지도 정보를 이용하여 최단 기간에 부대로 복귀
#다만, 적군의 방해로 인해 임무의 시작 때와 다르게 되돌아오는 경로가 없어져 복귀가 불가능할지도.

#n : 총지역 수 3~100,000  O(NlogN)
#roads : 두 지역을 왕복할 수 있는 길(길이 전부 1) 정보 2~500,000
#        [a,b] 형태 / [b,a] 존재 x
#sources : 각 부대원이 위치한 서로 다른 지역들을 나타내는 정수 배열 1~500
#destination : 강철부대의 지역 1~n

#answer : sources 순서대로 복귀 최단시간 담은 배열
#         복귀 불가능 하면 -1

def solution(n, roads, sources, destination):
    
    #roads 그래프 그리기
    #sources의 길이가 1부터 => n+1
    _map = [[] for _ in range(n+1)]
    for a, b in roads:
        _map[a].append(b)
        _map[b].append(a)
           
    #최단거리 찾기
    #도착지부터 모든 지점의 최단거리 구함 (첫 시작=destination) 
    queue = deque([destination])
    
    visit = [-1]*(n+1)
    visit[destination] = 0
    
    #BFS 한번에 구하기
    while queue:
        cur = queue.popleft()
        
        for n in _map[cur]:
            if visit[n] == -1:
                visit[n] = visit[cur] + 1
                queue.append(n)
                
    return [visit[i] for i in sources]
    
#solution(3,[[1,2],[2,3]],[2,3],1)


#풀이2
''' 테스트 11, 12, 13, 14, 15 시간초과 '''
#최악의 경우 ==> 10만*500번
#sources의 i 마다 BFS 구하기
'''
def make_map(_n, _roads):    
    # roads 정보 입력
    m_map = defaultdict(list)
    for a, b in _roads:
        m_map[a].append(b)
        m_map[b].append(a)
    return m_map


def bfs(m,start,final,visited, _n):
    dist = [0] * (_n+1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    if start == final:
        return 0
    while queue:
        start = queue.popleft()
        
        for cur in m[start]:
            if final in m[start]:
                cur = final
            if not visited[cur]:
                visited[cur] = True
                queue.append(cur)
                dist[cur] = dist[start] +1
                
                if cur == final:
                    queue.clear()
                    return dist[cur]
    return -1

def solution(n, roads, sources, destination):
    answer = []
    
    _map = make_map(n, roads)
    
    for source in sources:
        visit = [False] * (n+1)
        answer.append(bfs(_map, source, destination, visit, n))
    
    return answer

# deque 모듈 관련 : https://www.daleseo.com/python-queue/
'''
