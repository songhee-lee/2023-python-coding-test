#입력1 : .과 X로 이루어진 보드

#AAAA와 BB로 바꾸기

#출력 : 'X'를 폴리오미노, '.'는 냅둠
import sys

answer = []

str_in = input()
board = str_in.split('.')

flag = 0
for i in range(len(board)):
    cur = len(board[i])
    if cur % 2 == 1:
        print(-1)
        flag = 1
        break
    elif cur > 4:
        for _ in range(cur//4):
            answer += 'AAAA'
        if cur % 4 == 2 :
            answer += 'BB'
        
    elif cur == 4:
        answer += 'AAAA'
    elif cur == 2:
        answer += 'BB'

    if i < len(board) -1:
        answer += '.'

if flag == 0:
    print(''.join(answer))
