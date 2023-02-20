"""Psuedo Code
https://school.programmers.co.kr/learn/courses/30/lessons/60061

*. 기둥 & 보를 설치하거나 삭제 작업 진행
    - 삭제할 때 규칙 만족 안하면 해당 작업 무시
*. 모든 명령 수행 후 구조물의 상태를 return
    - (가로 좌표, 세로 좌표, 구조물 종류)
    - x 좌표 -> y 좌표 -> 구조물 종류(기둥 -> 보) 순으로 오름차순 정렬

- 기둥 (위로 설치)
    - 바닥 위 : x 좌표가 0
    - 보의 한쪽 끝 부분 위 : (x, y, 1) 또는 (x-1, y, 1) 
    - 다른 기둥 위 : (x, y-1, 0)
- 보 (오른쪽으로 설치)
    - 한 쪽 끝 부분이 기둥 위 : (x, y-1, 0) 또는 (x+1, y-1, 0) 
    - 양쪽 끝 부분이 다른 보와 동시에 연결 : (x, y, 1) and (x+1, y, 1) 

- 기둥 삭제
    - 기둥 위 기둥이 있거나, 기둥 위 보가 있으면 삭제 불가능

"""

def possibility_add(answer, order):
    
    x, y, a = order
    
    if a == 0 :     # 1. 기둥
        # 1) 바닥 위 or 2) 보의 한쪽 끝 부분 위 or 3) 다른 기둥 위
        if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
            return True

    elif a == 1:    # 2. 보
        # 1) 한 쪽 끝 부분이 기둥 위 or 2) 양쪽 끝 부분이 다른 보와 동시에 연결    
        if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
            return True

    return False

def possibility_remove(answer):
   
    for x, y, a in answer : 
        if a == 0 :     # 1. 기둥
            # 1) 바닥 위 or 2) 보의 한쪽 끝 부분 위 or 3) 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
                
            return False
        elif a == 1:    # 2. 보
            # 1) 한 쪽 끝 부분이 기둥 위 or 2) 양쪽 끝 부분이 다른 보와 동시에 연결    
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
                continue
            return False
        
    return True


def solution(n, build_frame):

    answer = []
    for x, y, a, b in build_frame:
        
        if b == 1 :     # 구조물 추가 작업
            if possibility_add(answer, (x, y, a)): # 추가 후 불가능하면 삭제
                answer.append([x, y, a]) 

        else :          # 구조물 삭제 작업
            answer.remove([x, y, a])    # 삭제 후 불가능하면 다시 추가
            if not possibility_remove(answer):
                answer.append([x, y, a])
            
    # 정렬
    return sorted(answer)