'''
[90도 회전 알고리즘]
* N은 배열의 크기(가로,세로 같다고 가정)
- 회전 후의 행 인덱스 = 회전 전의 열 인덱스 
- 회전 후의 열 인덱스 = N - 1 - 회전 전의 행 인덱스
'''
'''
열쇠로 자물쇠를 열 수 있다 => True => 자물쇠의 모든 칸은 값이 1이다.
열쇠로 자물쇠를 열 수 없다 => False => 자물쇠의 모든 칸의 값이 1은 아니다.
열쇠는 자물쇠의 영역을 벗어날 수 있다(=주어진 크기 범위를 벗어날 수 있다) => 기존 자물쇠의 크기를 변경해야 한다.

✅Flow - Time Complexity : O(N^4)
1. Key를 회전시킨다. ( 회전 횟수는 4번이다. 90도 -> 180도 -> 270도 -> 360도(초기 상태) )
2. 범위에 맞게 Lock에 Key 값을 더한다.
3. Lock의 모든 칸의 값이 1이라면 return True
4. 만약, (3)이 아니라면 Lock에 더한 Key값을 다시 뺴준다.
5. 다시 (1)로 돌아간다.
'''
def rotate(key): # Key 회전 함수 - O(M^2) 
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[j][m - i - 1] = key[i][j]
    return new_key

def check(new_lock): # 자물쇠의 모든 칸이 전부 돌기(=1)인지 확인 - O(N^2)
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)] # 새로운 자물쇠
    
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j] # 새로운 자물쇠의 가운데에 기존 자물쇠 위치시킨다.
            
    for _ in range(4): # 회전
        key = rotate(key)
        for i in range(1, n * 2): # 행(왼쪽, 오른쪽) 이동 - Lock
            for j in range(1, n * 2): # 열(위, 아래) 이동 - Lock
                for x in range(m): # 행(왼쪽, 오른쪽) 이동 - Key
                    for y in range(m): # 열(위, 아래) 이동 - Key
                        new_lock[i + x][j + y] += key[x][y] # new_lock에 key값을 더한다.(모두 1인지 확인하기 위함)

                if check(new_lock): # 새로운 자물쇠 확인
                    return True

                # Key로 new_lock을 열 수 없는 경우
                for x in range(m): 
                    for y in range(m):
                        new_lock[i + x][j + y] -= key[x][y] # 열 수 없는 경우이므로 new_lock의 값을 원래대로 돌린다.
    return False