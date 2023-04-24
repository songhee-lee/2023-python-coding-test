'''
- 2차원 리스트의 누적 합 사용
    - 2차원 리스트 arr이 있을 때, 
    - arr[x1][y1]부터 arr[x2][y2]까지의 부분 배열의 합을 Range(x1, y1, x2, y2)라 하자. 
    - 그리고 누적합 배열 S로 다음과 같이 정의된다.
    -> Range(x1, y1, x2, y2) = S(x2, y2) - S(x1, y2) - S(x2, y1) + S(x1, y1)
    
- skill에 대하여, 각각의 경우의 누적합을 구한다.
- 기존 board와 누적합을 합친다.
- 파괴되지 않은 건물의 개수를 카운트해서 return 한다.

- 정확성 : 1 <= n <= 100 / 1 <= m <= 100 / 1 <= skill <= 100 => 100 * 100 * 100 => 1,000,000 => O(N^3) 가능
- 효율성 : 1 <= n <= 1,000 / 1 <= m <= 1,000 / 1 <= skill <= 250,000 => O(N^3) 불가능

- 첫 시도: 정확성 ⭕️, 효율성 ❌
'''

# 누적합 구하는 함수
def get_prefix_sum(skill, prefix_sum, n, m):
    # 누적합 기록
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # 공격
            prefix_sum[r1][c1] -= degree
            prefix_sum[r1][c2 + 1] += degree
            prefix_sum[r2 + 1][c1] += degree
            prefix_sum[r2 + 1][c2 + 1] -= degree
        else: # 수리
            prefix_sum[r1][c1] += degree
            prefix_sum[r1][c2 + 1] -= degree
            prefix_sum[r2 + 1][c1] -= degree
            prefix_sum[r2 + 1][c2 + 1] += degree
    
    # 행 기준 누적합
    for i in range(n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] += prefix_sum[i][j - 1]
    
    # 열 기준 누적합
    for j in range(m + 1):
        for i in range(1, n + 1):
            prefix_sum[i][j] += prefix_sum[i - 1][j]
            
def solution(board, skill):
    answer = 0 # 파괴되지 않은 건물 개수
    n = len(board) # 행의 길이
    m = len(board[0]) # 열의 길이
    
    # 누적합 배열 초기화
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 누적합 구하기
    get_prefix_sum(skill, prefix_sum, n, m)
    
    # 기존 배열과 누적합 합치기
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix_sum[i][j]
            
            # 파괴되지 않은 건물 개수 세기
            if board[i][j] > 0: answer += 1
            
    return answer