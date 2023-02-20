'''
[조건]
- 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
- 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

Flow✅
1. build_frame을 순회하면서, (x, y, a)를 "먼저" 추가 or 삭제한다.
2. 먼저 추가 or 삭제를 한 후에 구조물이 만들어질 수 있는지 확인한다.
3. 만약, 만들어질 수 없다면 삭제 or 추가 한다.
4. build_frame을 모두 순회할 때 까지 (1)로 돌아가 반복한다.

** 삭제, 추가를 각각 함수로 구현할 수 있다.
    -> 너무 복잡해진다. 
    -> 따라서, 하나의 frame마다 (x, y, a)가 저장되어 있는 Set을 살펴본다.
    (= 처음 원소부터 끝 원소까지 돌면서, 추가 or 삭제했을 떄 구조물을 만들 수 있는지 없는지를 확인한다.)
'''

def can_build(ret): # 구조물이 만들어질 수 있는지 확인
    for x, y, a in ret:
        if a == 0: # 기둥 확인 
            if y == 0 or (x - 1, y, 1) in ret or (x, y, 1) in ret or (x, y - 1, 0) in ret: # 바닥인지, 왼쪽 보의 위에 있는지, 오른쪽 보의 위에 있는지, 기둥 위에 있는지
                continue
            return False
        elif a == 1: # 보 확인
            if (x, y - 1, 0) in ret or (x + 1, y - 1, 0) in ret or (x - 1, y, 1) in ret and (x + 1, y, 1) in ret: # 왼쪽 기둥이 있는지, 오른쪽 기둥이 있는지, 왼쪽 보와 오른쪽 보가 둘 다 있는지
                continue
            return False
    return True

def solution(n, build_frame):
    ret = set()
    for x, y, a, b in build_frame:
        frame = (x, y, a)
        if b == 1: # 설치
            ret.add(frame) # 먼저 추가한다.
            if not can_build(ret): # 지을 수 없다면
                ret.remove(frame) # 제거한다.
        elif b == 0: # 삭제
            ret.remove(frame) # 먼저 삭제한다.
            if not can_build(ret): # 지을 수 없다면
                ret.add(frame) # 제거한다.
    ans = list(map(list, ret))
    ans.sort(key=lambda x:(x[0], x[1], x[2])) # x좌표, y좌표, 기둥 순으로 정렬한다.
    return ans


# '''
# 실패한 코드
# '''

# def i_column_check(row, col, n, x, y): # 바닥인지, 아래 기둥있는지, 보 위에 있는지 확인
#     if x == n or col[x + 1][y] == 0 or row[x][y - 1] == 1 or row[x][y] == 1:
#         return True
#     return False
# def d_column_check(row, col, x, y): # 위에 기둥이 있는지
#     if col[x - 1][y] == 0:
#         return False
#     if row[x - 1][y + 1] == 1:
#         if col[x][y - 1] != 0:
#             return False
#     if row[x - 1][y] == 1:
#         if col[x][y + 1] != 0:
#             return False
#     return True

# def i_row_check(row, col, x, y): # 보의 한쪽 끝 부분이 기둥 위인지, 양쪽 끝 부분이 다른 보와 연결되어 있는지 확인
#     if col[x + 1][y] == 0 or col[x + 1][y + 1] == 0:
#         return True
#     if row[x][y - 1] == 1 and row[x][y + 1] == 1:
#         return True
#     return False

# def d_row_check(row, col, x, y):
#     if row[x][y - 1] == 1:
#         if col[x + 1][y - 1] != 0 and col[x + 1][y] != 0:
#             return False
#     if row[x][y + 1] == 1:
#         if col[x + 1][y + 1] != 0 and col[x + 1][y + 2] != 0:
#             return False
#     return True
# def solution(n, build_frame):
#     col = [[-1] * (n + 1) for _ in range(n + 1)] # 기둥
#     row = [[-1] * (n + 1) for _ in range(n + 1)] # 보
    
#     for frame in build_frame:
#         x, y, a, b = frame
#         new_x = n - y - 1
#         new_y = x
#         if b == 1: # 설치
#             if a == 0: # 기둥 이라면
#                 if i_column_check(row, col, n, new_x, new_y):
#                     col[new_x][new_y] = 0
#                 else:
#                     continue
#             elif a == 1:
#                 if i_row_check(row, col, new_x, new_y):
#                     row[new_x][new_y] = 1
#                 else:
#                     continue
#         elif b == 0: # 삭제
#             if a == 0: # 기둥 이라면
#                 if d_column_check(row, col, new_x, new_y):
#                     col[new_x][new_y] = -1
#             elif a == 1:
#                 if d_row_check(row, col, new_x, new_y):
#                     row[new_x][new_y] = -1
#     print(col)
#     answer = [[]]
#     return answer