# DFS : 현재 위치의 값이 '0'이고 현재 위치를 방문한 적이 없으면 계속 탐색하는 함수
def check(tray, visited, visit, i,j):
    if tray[i][j] == '0' and not visited[i][j] : 
        # 현재 위치 방문처리
        visited[i][j] = True
        visit.append((i,j)) # 방문 내역 update

        # 상하좌우 탐색
        if i-1 >= 0 : check(tray,visited,visit,i-1,j)  # 상
        if i+1 < N  : check(tray,visited,visit,i+1,j)  # 하
        if j-1 >= 0 : check(tray,visited,visit,i,j-1)  # 좌
        if j+1 < M  : check(tray,visited,visit,i,j+1)  # 우


# 입력 : 얼음 틀 세로 길이 N, 가로 길이 M, 얼음 틀 형태 Tray
N,M = map(int,input().split()) # 얼음 틀 가로, 세로 길이
tray = []       # 얼음 틀 형태
visited = []    # 방문 여부 확인용
count = 0       # 아이스크림 개수
for n in range(N):
    tray.append(list(input()))   # 얼음 틀 형태 update
    visited.append([False]*M)    # 방문 여부 초기화

# 완전 탐색
for n in range(N):
    for m in range(M):
        # check 함수로 탐색 후, 0이 하나라도 있었으면(방문한 적이 있었으면) 아이스크림 개수 1 증가
        visit = []      # 방문한 곳 내역
        check(tray, visited, visit, n,m)
        if visit: count += 1

print(count)