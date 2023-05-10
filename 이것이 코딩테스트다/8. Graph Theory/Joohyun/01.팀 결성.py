"""
학생 : 0번 ~ N번 (N+1명)
서로 다른 팀 -> 
연산 종류 : 2가지
1) 팀 합치기
2) 같은 팀 여부 확인

M번의 연산
'같은 팀 여부 확인' 연산에 대한 연산 결과 출력
"""

n,m = map(int,input().split())      # n:번호, m:연산 수
students=[i for i in range(n+1)]    # 학생들의 팀, 초기화

def union_team(students,a,b):
    a_=students[a]
    b_=students[b]

    if a_<b_:students[b]=a_
    elif a_>b_:students[a]=b_

for _ in range(m):
    # 연산 cal=0이면 합치기, cal=1이면 여부 확인
    cal,a,b=map(int,input().split()) # a와 b번 학생 팀 연산
    if cal==1:  # '같은 팀 여부 확인'
        if students[a]==students[b]:print('YES')
        else:print('NO')
    else:       # '팀 합치기'
        union_team(students,a,b)
