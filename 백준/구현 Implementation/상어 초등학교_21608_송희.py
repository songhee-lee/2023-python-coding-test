# 입력 받기
N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]

# 초기 세팅
maps = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

# 학생 순서대로 앉히기
for num in range(N**2) :
    student = students[num]
    
    # 앉을 수 있는 자리 찾기
    candidates = [] 
    for i in range(N) :
        for j in range(N) :
            if maps[i][j] == 0 :
                like, blank = 0, 0
                for d in range(4) :
                    nx, ny = i+dx[d], j+dy[d]
                    if 0 <= nx < N and 0 <= ny < N :
                        if maps[nx][ny] == 0 :              # 빈 칸
                            blank += 1
                        elif maps[nx][ny] in student[1:] :  # 다른 학생이 앉음
                            like += 1
                candidates.append([like, blank, i, j])
    
    # 좋아하는 학생 수 -> 비어있는 칸 수 -> 행 번호 -> 열 번호
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    maps[candidates[0][2]][candidates[0][3]] = student[0]

# 학생 만족도 구하기
answer = 0
students.sort()

for i in range(N) :
    for j in range(N) :
        score = 0
        for d in range(4) :
            nx, ny = i+dx[d], j+dy[d]
            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] in students[maps[i][j]-1] :
                score += 1
        if score != 0 :
            answer += 10 ** (score-1)

print(answer)