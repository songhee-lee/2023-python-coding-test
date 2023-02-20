# 열쇠를 시계방향으로 90도씩 회전하는 함수 생성
# zip함수를 이용해 열쇠의 각 행과 열을 바꿔줌
# 열쇠 이동함수 생성

def rotate(key):
    # 90도 회전
    m = len(key)
    rotated_key = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated_key[j][m-1-i] = key[i][j]
    return rotated_key


def check(lock, n):
    # 자물쇠가 열리는지 확인
    for i in range(n):
        for j in range(n):
            if lock[i+n][j+n] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 lock 생성
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                # key를 new_lock의 (x, y) 위치에 놓고 확인
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock, n):
                    return True
                # key를 new_lock의 (x, y) 위치에 놓고 확인 후 다시 원상복구
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
