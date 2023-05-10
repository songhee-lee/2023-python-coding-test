'''
[문제]
- 노트에 n명의 이름을 적을 때 다음 조건을 만족해야 한다.
    1. 이름은 이미 정해진 순서대로 n명의 이름을 넣는다.
    2. 노트의 위에서 아래로, 같은 줄에서는 왼쪽 맨 끝에서 오른쪽으로 차례로 적는다.
    3. 이름을 적을 때 각 사람의 이름 사이에 빈칸을 하나씩 둬야 한다.
    4. 한 줄을 적다가 그 줄의 끝에 한 사람의 이름이 다 들어가지 않고 잘리게 되면,
        반드시 새로운 줄에 이름을 써야 한다.
- 이때 각 줄의 끝에 사용하지 않고 남게 되는 칸의 수의 제곱의 합이 최소가 되도록 하려 한다.
- 마지막 줄은 앞으로 이름을 적을 기회가 있으므로 계산하지 않는다.

[점화식]
- dp[idx] = min(dp[idx], left_cell**2 + helper(i))
    -> idx + 1번째 이름을 새로운 줄에 적을 때, 남은 공간들의 제곱합의 최솟값
    

✅ 답 참고함, 다시 풀어보기
'''
import sys
sys.setrecursionlimit(10000)


# sol 2
def sol2():
    # Top-Down 방식
    def helper(idx):
        
        # 이미 값을 저장했다면, 그 값을 반환한다.
        if dp[idx] != float('inf'):
            return dp[idx]
        
        # 남은 칸의 수(전체 너비는 m이고 현재 이름의 길이를 빼준다.)
        left_cell = m - names[idx]
        
        # 이름을 계속 이어 붙인다.
        for i in range(idx + 1, n + 1):
            # 만약, 칸이 남아 있다면
            if left_cell >= 0:
                # 만약, 마지막 이름이라면 => 새로운 줄을 만들지 않고 한 줄에 이어붙인 경우
                # 마지막 줄을 의미하므로 dp[idx] = 0으로 초기화한다.
                if i == n:
                    dp[idx] = 0
                    break
                
                # 재귀 호출
                dp[idx] = min(dp[idx], left_cell**2 + helper(i))
                
                # 남은 칸의 개수 갱신
                # names[i]를 이어 붙였으므로, 해당 이름의 길이와 빈 칸 1을 빼준다.
                left_cell -= names[i] + 1
            
        return dp[idx]
        
    # dp 테이블 초기화
    dp = [float('inf')] * n
    dp[n - 1] = 0
    
    print(helper(0))

n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]

sol2()

# sol 1 - 시간 초과
# def sol1():    
    
#     def helper(idx, _len):
#         if dp[idx][_len] != -1:
#             pass
#         else:
#             if idx == n - 1:
#                 dp[idx][_len] = 0
#             else:
#                 if idx + 1 + names[idx + 1] < m:
#                     dp[idx][_len] = min(helper(idx + 1, idx + 1 + names[idx + 1]), helper(idx + 1, names[idx + 1] - 1) + (m - idx  - 1)**2)

#         return dp[idx][_len]
    
#     dp = [[-1] * (m) for _ in range(n)]
    
#     print(helper(0, names[0] - 1))
    