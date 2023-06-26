#정답률 0.95% 6번문제..

#카드 4x4 8종류 2개씩
#2장 선택해서 같은 그림이면 사라짐
#같은 그림이 아니면 다시 뒷면


#카드는 '커서'를 이용해서 선택
# 커서는 컨트롤키와 방향키에 의해 이동
#   방향키 : 커서가 키 방향으로 1칸 이동
#   컨트롤+방향키 : 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동
#   if 해당 방향에 카드가 없으면 그 방향의 가장 마지막 칸으로 이동
#   if 누른 키 방향으로 이동 가능한 카드 또는 빈 공간이 없어 이동할 수 없다면 커서는 움직이지 않음

# 커서가 위치한 카드를 뒤집기 위해서는 엔터 키 입력

# 목표 : 몇 장 제거된 상태에서 카드 앞면의 그림을 알고 있다면, 
#        남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값 구하기

# 조작 횟수 1 : 엔터, 방향키, 컨+방향키

# board : 0은 빈칸, 1~6이 2개씩 들어있음 / 모두 0인 경우는 없음

#1,6,8,9,10,13,14,16,17,18,21,24,27,29,30 통과
from itertools import permutations
from collections import deque
from copy import deepcopy
board = []
def control(_r,_c,dx,dy):
    global board
    
    while True:
        new_r = _r + dx
        new_c = _c + dy

        # 이동했을 때 끝이면 리턴
        if not (0<= new_r <4 and 0<=new_c<4):
            return _r, _c
        
        if board[new_r][new_c] != 0:
            return new_r, new_c

        _r = new_r
        _c = new_c

def min_dist(start, end):
    r, c = start
    find_r, find_c = end

    queue = deque()
    queue.append((r,c,0))
    
    visited = [[0] * 4 for _ in range(4)]
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    while queue:
        r, c, temp = queue.popleft()
        
        if visited[r][c] == 1 : 
            continue
            
        visited[r][c] = 1
        #도착 break
        if r == find_r and c == find_c:
            return temp
        
        for i in range(4):
            cur_r = r + dx[i]
            cur_c = c + dy[i]
            
            if 0<= cur_r <4 and 0<=cur_c<4:
                queue.append((cur_r, cur_c, temp + 1))
                
            cur_r, cur_c = control(r,c,dx[i],dy[i])
            
            queue.append((cur_r, cur_c, temp + 1))

    return -1

def solution(input_board, r, c):
    global board
        
    board = input_board
    
    #dict 에 모든 카드의 위치 저장
    dic = [[] for _ in range(7)]
    

    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                dic[board[i][j]].append((i,j))

                max_num = max(max(input_board))
    
    #순열
    per_list = [i for i in range(max_num+1) if i not in {0}]
    per = list(permutations(per_list,max_num))
    
    answer = float('inf')

    #모든 경우의 수에 대하여
    for i in range(len(per)):
        board = deepcopy(input_board)
        cnt = 0

        for j in per[i]:
            card1 = min_dist((r,c), dic[j][0]) #카드 1까지 거리
            card2 = min_dist((r,c), dic[j][1]) #카드 2까지 거리
            if card1 < card2:
                cnt += card1 #카드 1까지 거리
                cnt += min_dist(dic[j][0], dic[j][1]) #같은 카드까지 거리
                r,c = dic[j][1] #같은 카드로 위치 변경
            else :
                cnt += card2
                cnt += min_dist(dic[j][1], dic[j][0])
                r,c = dic[j][0] 
            # 맞춘 카드 지우기
            board[dic[j][0][0]][dic[j][0][1]] = 0
            board[dic[j][1][0]][dic[j][1][1]] = 0
            cnt+=2

        answer = min(answer, cnt)

    return answer

'''
#2,3,9,11,18,20,21 통과
# 이동하기 위한 거리
def dist(r,c,_r,_c):
    
    # 행이나 열이 같으면 1번 움직임
    if _r == r  or _c == c:
        return 1
                
    # 행과 열이 모두 다르면 
    # 끝에 있을 경우 컨트롤+ 움직임 2번
    if (_r == 3 or _r == 0) and (_c == 3 or _c == 0):
        return 2
    
    # 한 방향만 끝에 있을 경우 
    if _r == 3 or _r == 0 :
        # 1번 + c값 차이
        return 1 + abs(_c-c)
    if _c == 3 or _c == 0:
        # 1번 + r값 차이
        return 1 + abs(_r-r)
    
    #최악의 경우 r값/c값 차이
    return abs(_r-r) + abs(_c-c)


# 가장 가까운 그림으로 이동
def min_distance(dic, r, c):
    distance = [0] * 7  # 그림은 최대 6개 까지있음
    min_dist = []
    
    for key in range(6):
        if len(dic[key]) < 2 :
            min_dist.append(0)
            continue

        d1 = dist(r,c,dic[key][1][0],dic[key][1][1]) #value1과 r,c 거리
        d2 = dist(r,c,dic[key][2][0],dic[key][2][1]) #value2과 r,c 거리

        if d1 < d2:
            distance[dic[key][0]] = d1
            min_dist.append(dic[key][1])
        elif d1 > d2:
            distance[dic[key][0]] = d2
            min_dist.append(dic[key][2])
        elif d1 == d2:
            same1 = abs(dic[key][1][0]-r) + abs(dic[key][1][1]-c)
            same2 = abs(dic[key][2][0]-r) + abs(dic[key][2][1]-c)
            if same1 < same2 : 
                distance[dic[key][0]] = d1
                min_dist.append(dic[key][1])
            else :
                distance[dic[key][0]] = d2
                min_dist.append(dic[key][2])
            


    remove_dist = [i for i in distance if i not in {0}]
    result_move = min(remove_dist)
    result_rc = min_dist[distance.index(result_move)]
    return result_rc[0], result_rc[1], result_move

# 같은 그림으로 이동
def find(dic,num, r,c):
    _r = dic[num][1][0]
    _c = dic[num][1][1]
    
    if r == _r and c == _c :
        _r = dic[num][2][0]
        _c = dic[num][2][1]

    #dic에서 r,c / _r,_c 둘다 삭제
    del dic[num][1]
    del dic[num][1]

    d = dist(r,c,_r,_c)
    
    return _r,_c, d, dic

def solution(board, r, c):
    answer = 0
    
    #엔터 횟수 = 제일 큰 숫자 x 2
    answer += max(max(board)) * 2 
    
    #dict 에 모든 카드의 위치 저장
    dic = [[i] for i in range(6)]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] >0:
                dic[board[i][j]].append([i,j])

    print(r,c)
    while (any([any(board[i]) for i in range(4)])) :
        # 현재 위치에 그림이 있을 경우
        if board[r][c] > 0 :
            _r,_c = r, c
            r, c, move, dic = find(dic, board[r][c], r, c)
            board[_r][_c], board[r][c] = 0, 0

            answer += move

        # 현재 위치에 그림이 없을 경우
        elif board[r][c] == 0:
            r, c, move = min_distance(dic,r,c)
            print(r,c,move)

            answer += move
        
    return answer

#solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)
#solution([3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1)
'''