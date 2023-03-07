# 막대 3종류 : A, B, C
# 원판 3종류 : A, B, C (크기는 같다)
# 시작 시  : 각 막대에는 0개 이상의 원판이 있음
# 동작 로직 : 막대 가장 위에 있는 원판을 다른 막대의 가장 위로 옮긴다
# 목표 : A막대&A원판, B막대&B원판, C막대&C원판
# 움직임 최소 횟수
# 입력 : 원판개수, 원판상태

import collections

arr = [input()[2:] for _ in range(3)]   # 막대별 원판 상태
print(arr)
visited = collections.defaultdict(int)
q = collections.deque()

q.append((arr[0],arr[1],arr[2],0))      # A막대 원판상태, B막대 원판상태, C막대 원판상태, 이동횟수

while q:
    a,b,c,cnt = q.popleft()             # A막대 원판상태, B막대 원판상태, C막대 원판상태, 이동횟수
    status = a + '/' + b + '/' + c      # 막대별 원판상태 (구분자 : /) 

    # 막대-원판끼리 일치하면 종료
    if 'B' not in a and 'C' not in a :
        if 'A' not in b and 'C' not in b:
            if 'A' not in c and 'B' not in c:
                print(cnt)
                exit(0)

    # 현재 원판-막대 상태에 방문한적 없다면 (이 상태로 옮긴 적이 없으면)
    if not visited[status]:
        visited[status] += 1    # 방문

        if len(a) > 0:  # 막대 A에 원판이 있을 경우
            q.append((a[:-1], b+a[-1], c, cnt+1))   # A 가장 위 원판 -> B 가장 위
            q.append((a[:-1], b, c+a[-1], cnt+1))   # A 가장 위 원판 -> C 가장 위
        if len(b) > 0:  # 막대 B에 원판이 있을 경우
            q.append((a+b[-1], b[:-1], c, cnt+1))   # B 가장 위 원판 -> A 가장 위
            q.append((a, b[:-1], c+b[-1], cnt+1))   # B 가장 위 원판 -> C 가장 위
        if len(c) > 0:  # 막대 C에 원판이 있을 경우
            q.append((a+c[-1], b, c[:-1], cnt+1))   # C 가장 위 원판 -> A 가장 위
            q.append((a, b+c[-1], c[:-1], cnt+1))   # C 가장 위 원판 -> B 가장 위

print(-1)