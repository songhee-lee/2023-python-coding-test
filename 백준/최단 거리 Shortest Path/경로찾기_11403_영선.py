#입력1 : 노드 n
#입력2 : i j 0 이면 없음 i j 1 이면 있음 (자기자신으로 돌아오는 경로 없음)

#모든 정점(i,j)에 대해서 i에서 j로 가는 길이가 양수인 경로가 있는지 구하기

#정점 i에서 j로 가는 길이가 양수인 경로가 있으면 (i,j)를 1로 없으면 0으로
import sys
n = int(input())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 


#플로이드 와샬?

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
    print()
