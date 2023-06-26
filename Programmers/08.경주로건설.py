from collections import deque
import math

def solution(board):
    def bfs(start_x, start_y, start_cost, start_dir):
        n = len(board)
        result = [[math.inf for _ in range(n)] for _ in range(n)]  # 최소 비용을 저장할 배열 초기화
        queue = deque()
        queue.append((start_x, start_y, start_cost, start_dir))
        result[start_x][start_y] = 0  # 시작 위치의 비용을 0으로 설정
        while queue:
            x, y, cost, direction = queue.popleft()
            for i in range(4):
                dx = [-1, 1, 0, 0]  # 상하좌우 방향을 나타내는 x 좌표 변화값
                dy = [0, 0, -1, 1]  # 상하좌우 방향을 나타내는 y 좌표 변화값
                new_x, new_y, new_cost = x + dx[i], y + dy[i], cost + 600 if i != direction else cost + 100
                if 0 <= new_x < n and 0 <= new_y < n and board[new_x][new_y] == 0 and result[new_x][new_y] > new_cost:
                    result[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, i))  # 새로운 위치와 비용을 큐에 추가
        return result[-1][-1]  # 마지막 위치의 최소 비용 반환

    return min(bfs(0, 0, 0, 0), bfs(0, 0, 0, 2))  # 오른쪽 방향과 아래쪽 방향에서 시작하는 BFS 탐색 후 최소 비용 반환