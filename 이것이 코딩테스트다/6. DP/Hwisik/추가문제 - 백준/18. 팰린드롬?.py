'''
[문제]
- 자연수 N개를 칠판에 적는다, 질문을 총 M번 한다.
- 각 질문은 두 정수 S와 E로 나타낸다. S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지 아닌지를 묻는다.
- 예를 들어, 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.
    S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
    S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
    S = 3, E = 3인 경우 1은 팰린드롬이다.
    S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
    
[점화식]
- 

✅ PyPy3로 제출해야 시간초과가 발생하지 않는다.
'''
# 수열의 크기
n = int(input())
nums = list(map(int, input().split()))

# 질문의 개수
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(n)]

# sol - 1
for _len in range(n): # 팰린드롬의 길이
    for start in range(n - _len): # 시작점
        end = start + _len # 끝점
        
        # 자기 자신은 팰린드롬
        if _len == 0:
            dp[start][end] = 1
        # 시작점과 끝점이 같다면
        elif nums[start] == nums[end]:
            # 길이가 2 이하라면 팰린드롬
            if _len < 3: dp[start][end] = 1 
            
            # 길이가 3 이상이고, 시작과 끝을 제외한 사이의 값이 팰린드롬이라면
            elif dp[start + 1][end - 1] == 1: dp[start][end] = 1
################################################################################

# sol - 2

# 자기 자신은 팰린드롬
for i in range(n):
    dp[i][i] = 1

# 길이가 2인 팰린드롬
for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

# 길이가 3이상일 때는 점화식 사용
for _len in range(3, n + 1):
    for i in range(n - _len + 1): # 시작점
        j = i + _len - 1 # 끝점
        
        # 시작점과 끝점이 같고, 시작과 끝을 제외한 사이의 값이 팰린드롬이라면
        if nums[i] == nums[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1


# 질문지 확인                   
for query in queries:
    s, e = query
    if dp[s - 1][e - 1] == 1:
        print(1)
    else:
        print(0)