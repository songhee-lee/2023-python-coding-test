'''
n: 컴퓨터의 개수 <=200
computers : 연결 정보 2차원 배열 [i][j] == 1
            [i][i] == 항상 1
            (그래프)
네트워크의 개수 return

연결 없이 혼자 존재하는 컴퓨터도 1개의 네트워크
'''

def DFS(v, visited, graph):    
    visited[v] = True
    
    for i, e in enumerate(graph[v]):
        #자기 자신이 아니고 visit 가 false 이고 값이 1인 것
        if (v != i) and (visited[i] == False) and (e==1):
            DFS(i, visited, graph)
            
    return visited
  
            
def solution(n, computers):
    visited = [False] * n
    answer, start = 0, 0
    visited = DFS(start, visited, computers)
    answer += 1

    while True:
        if False in visited:
            start = visited.index(False)
            visited = DFS(start, visited, computers)
            answer += 1
        else:
            break

    return answer

