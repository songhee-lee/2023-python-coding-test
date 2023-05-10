"""Psuedo Code
https://school.programmers.co.kr/learn/courses/30/lessons/60059

0 홈 1 돌기

1. 자물쇠를 N x N 에서 열쇠 크기를 포함한 (N+2*M-2) x (N+2*M-2) 로 확장
2. 열쇠를 회전+이동 하면서 자물쇠와 맞는지 확인하기
    - 열쇠 돌기랑 자물쇠 홈 일치
    - 모든 자물쇠의 홈이 채워져야 함
    - 열쇠 돌기랑 자물쇠 돌기 만나면 안됨


"""
import copy 

def lock_expand(M, lock):
    # 자물쇠 확장하기
    # N x N -> (N+ 2*M-2) x (N+ 2*M-2)

    N = len(lock)
    lock_new = [[0 for _ in range(N + 2*M - 2)] for _ in range(N + 2*M - 2)]
    
    for i in range(N):
        for j in range(N):
            lock_new[i + M - 1][j + M -1 ] = lock[i][j] 
    
    return lock_new

def check(key, lock, loc):
    # 자물쇠랑 열쇠 맞는지 확인하기

    x, y = loc[0], loc[1]   # 확장된 자물쇠에서 위치
    M = len(key)            # key 크기
    N = len(lock) - 2*(M-1) # 원래 자물쇠 크기

    # lock에 key 값 더하기
    for i in range(M):
        for j in range(M):
            lock[i+x][j+y] += key[i][j]


    # 모든 자물쇠의 홈 채워졌는 지 확인
    for i in range(M-1, M+N-1):
        for j in range(M-1, N+M-1):
            if lock[i][j] != 1:
                return False
    
    return True


def rotate(key):
    # 자물쇠 90도 회전하기
    M = len(key)
    new_key = [[0] * M for _ in range(M) ]

    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[M-1-j][i]

    return new_key


def solution(key, lock):

    N, M = len(lock), len(key)  # 자물쇠 크기, key 크기

    # 1. 자물쇠를 열쇠 크기 포함해 확장
    lock_new = lock_expand(M, lock)
    
    # 2. 열쇠 회전+이동 하면서 확인하기
        # 열쇠 회전한 리스트
    key_list = [key, ]
    key_list.append(rotate(key))
    key_list.append(rotate(key_list[1]))
    key_list.append(rotate(key_list[2]))

    for i in range(N+M-1):
        for j in range(N+M-1):
            for k in range(4):
                if check(key_list[k], copy.deepcopy(lock_new), (i,j)):
                    return True
    

    return False

