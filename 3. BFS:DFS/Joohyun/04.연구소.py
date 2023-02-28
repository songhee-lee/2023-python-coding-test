# 해설 코드
# 연구소 크기 : N * M
# 바이러스 : 상하좌우 인접한 빈칸으로 퍼져나간다
# 세워야 하는 벽의 개수 : 3개
# 0 : 빈칸, 1 : 벽, 2 : 바이러스
# 바이러스 개수 : 2 이상, 10 이하
# 안전 영역의 크기 최댓값 ?

# 벽설치 완전탐색
# 벽 설치 후 바이러스 전염 : DFS 로 처리

# 입력 : 연구소 크기, 지도 정보
N, M = map(int,input().split())
Map = [] # 지도 정보 : 빈칸 0, 벽 1, 바이러스 2
for n in range(N):
    Map.append(list(map(int,input().split())))
temp = [[0]*M for n in range(N)] # 벽을 설치한 뒤의 맵 리스트

# 4가지 이동 방향에 대한 리스트 : 상하좌우
dx = [-1,1,0,0]
dy = [0, 0,-1,1]

result = 0

# dfs -> 바이러스가 사방에 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >=0 and nx < N and ny >=0 and ny < M :
            if temp[nx][ny]==0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                    temp[nx][ny]=2
                    virus(nx,ny)

# 현재 맵에서 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                score += 1
    return score

# dfs -> 벽 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j]=Map[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                if temp[i][j]==2:virus(i,j)
        
        # 안전 영역 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if Map[i][j]==0:
                Map[i][j] =1
                count+=1
                dfs(count)
                Map[i][j]=0
                count-=1

dfs(0)
print(result)
