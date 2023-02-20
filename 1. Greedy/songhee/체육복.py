"""Pseudo Code
1. 도난 당한 학생 번호와 여벌 옷 있는 학생 번호 boolean 배열 만들기
2. 여벌 옷이 있는데, 본인이 도난 당한 경우 확인
3. 앞 번호 -> 뒷 번호 순으로 빌릴 수 있는 지 확인
"""

def solution(n, lost, reserve):
    answer = n - len(lost)    # 체육 수업 들을 수 있는 학생
    
    # 1. boolean 배열 만들기
    c_lost = [ 1 if x in lost else 0 for x in range(0, n+2) ]
    c_reserve = [ 1 if x in reserve else 0 for x in range(0, n+2) ]
    
    # 2. 여벌 옷이 있는데, 본인이 도난 당한 경우 확인
    for i in range(1, n+1) :
        if c_lost[i] and c_reserve[i]:
            answer += 1
            c_lost[i] = 0
            c_reserve[i] = 0

    # 3. 앞 번호 -> 뒷 번호 순으로 빌릴 수 있는 지 확인
    for i in range(1, n+1) :
        if c_lost[i] and c_reserve[i-1]:
            answer += 1
            c_lost[i] = 0
            c_reserve[i-1] = 0
        elif c_lost[i] and c_reserve[i+1]:
            answer += 1
            c_lost[i] = 0
            c_reserve[i+1] = 0

    return answer
    
    