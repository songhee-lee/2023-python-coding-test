def is_possible(table, x, y, a) :
    # 기둥 설치
    if a == 0 :
        # 1) 바닥이거나 2) 보의 한 쪽 끝 부분 위에 있거나 3) 다른 기둥 위에 있어야 한다.
        if y == 0 or (x, y, 1) in table or (x-1, y, 1) in table or (x, y-1, 0) in table:
            return True
    elif a == 1 :
        # 1) 한쪽 끝 부분이 기둥 위에 있거나 2) 다른 보와 동시에 연결
        if (x, y-1, 0) in table or (x+1, y-1, 0) in table or ((x-1, y, 1) in table and (x+1, y, 1) in table) :
            return True
    return False

def solution(n, build_frame):
    table = set()   # (x 좌표, y 좌표, 구조물 종류)
    
    for x, y, a, b in build_frame :
        # 설치
        if b == 1 and is_possible(table, x, y, a) :
                table.add((x, y, a))
        # 삭제
        elif b == 0 :
            # 해당 구조물을 삭한 뒤, 다른 구조물들이 모두 잘 설치될 수 있는지 확인하기
            table.remove((x, y, a))     
            for nx, ny, na in table :
                if (nx, ny, na) in table and not is_possible(table, nx, ny, na) :
                    table.add((x, y, a))
                    break

    
    return sorted(list(table))
