from collections import deque

answer = 1e9
def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = set()
    # 직사각형 테두리선의 각 좌표 추가하기
    for lx, ly, rx, ry in rectangle:
        for x in range(lx, rx):
            maps.add(((x, x+1), ly))
            maps.add(((x, x+1), ry))
                
        for y in range(ly, ry):
            maps.add((lx, (y, y+1)))
            maps.add((rx, (y, y+1)))
    
    # 직사각형 내부 선의 각 좌표 제거하기 (겹치는 부분들)
    for lx, ly, rx, ry in rectangle:
        for x in range(lx+1, rx):
            for y in range(ly, ry):
                if (x, (y, y+1)) in maps :
                    maps.remove((x, (y, y+1)))
        for y in range(ly+1, ry):
            for x in range(lx, rx):
                if ((x, x+1), y) in maps :
                    maps.remove(((x, x+1), y))
    
    # 최단거리 찾기
    visited = dict(zip(maps, [False]*len(maps)))    # 방문 배열
    q = deque([(characterX, characterY, 0)])
    
    while q:
        x, y, cnt = q.popleft()

        if x == itemX and y == itemY :  # 아이템에 도달한 경우 stop
            return cnt
        
        # 상하좌우 방향으로 이동한다.
        if ((x-1, x), y) in maps and not visited[((x-1, x), y)]:     # 좌
            q.append((x-1, y, cnt+1))
            visited[((x-1, x), y)] = True
        if ((x, x+1), y) in maps and not visited[((x, x+1), y)]:   # 우
            q.append((x+1, y, cnt+1))
            visited[((x, x+1), y)] = True
        if (x, (y, y+1)) in maps and not visited[(x, (y, y+1))]:   # 위
            q.append((x, y+1, cnt+1))
            visited[(x, (y, y+1))] = True
        if (x, (y-1, y)) in maps and not visited[(x, (y-1, y))]:   # 아래
            q.append((x, y-1, cnt+1))
            visited[(x, (y-1, y))] = True