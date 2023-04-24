'''
- min-max algorithm

- 풀이 참고(이해 불가)
- https://github.com/encrypted-def/kakao-blind-recruitment/blob/master/2022-blind/Q7.py
- https://velog.io/@mrbartrns/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%82%AC%EB%9D%BC%EC%A7%80%EB%8A%94-%EB%B0%9C%ED%8C%90-python
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = 0, 0

vis = [[0] * 5 for _ in range(5)]
block = [[0] * 5 for _ in range(5)]

# 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: return False
    return True

# 현재 상태에서 둘 다 최적의 플레이를 할 때 남은 이동 횟수
# 반환 값이 짝수 : 플레이어가 패배함을 의미
    # -> 앞으로 짝수번 더 이동한다. 나 - 상대 - 나 - 상대 .. 이므로 상대가 마지막으로 움직인 후 끝나므로, 상대가 먼저 이기게 됨
# 반환 값이 홀수 : 플레이어가 승리함을 의미
    # -> 앞으로 홀수번 더 이동한다. 상대 - 나 - 상대 - 나 .. 이므로 내가 마지막으로 움직인 후 끝나므로, 내가 먼저 이기게 됨
# curx, cury : 현재 플레이어의 좌표, opx, opy : 상대 플레이어의 좌표
# ret : 현재 저장된 턴 -> 해당 함수에서 반환할 값
# val : 새로 계산된 턴 -> 플레이어가 4개의 각 방향으로 이동했을 때 남은 이동 횟수
def helper(curx, cury, opx, opy):
    global vis, block
    
    # 플레이어가 밟고 있는 발판이 사라졌다면
    if vis[curx][cury]: return 0
    ret = 0
    
    # 플레이어를 네 방향으로 이동시켜 다음 단계로 진행할 예정
    for dir in range(4):
        nx = curx + dx[dir]
        ny = cury + dy[dir]
        
        if not is_range(nx, ny) or vis[nx][ny] or block[nx][ny] == 0: continue
        
        # 방문 표시
        vis[curx][cury] = 1
        
        # 플레이어를 dir 방향으로 이동시켰을 때 턴의 수
        # 다음 함수를 호출할 때 opx, opy, nx, ny 순으로 호출해야 함에 주의
        val = helper(opx, opy, nx, ny) + 1
        
        # 방문 표시 해제
        vis[curx][cury] = 0
        
        # 1. 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우
        if ret % 2 == 0 and val % 2 == 1: ret = val # 바로 갱신
        
        # 2. 현재 저장된 턴과 새로 계산된 턴이 모두 패배인 경우
        elif ret % 2 == 0 and val % 2 == 0: ret = max(ret, val) # 최대한 늦게 지는걸 선택
        
        # 3. 현재 저장된 턴과 새로 계산된 턴이 모두 승리인 경우
        elif ret % 2 == 1 and val % 2 == 1: ret = min(ret, val) # 최대한 빨리 이기는걸 선택
        
    return ret

def solution(board, aloc, bloc):
    global n, m
    
    # 행, 열 길이
    n, m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]
            
    return helper(aloc[0], aloc[1], bloc[0], bloc[1])