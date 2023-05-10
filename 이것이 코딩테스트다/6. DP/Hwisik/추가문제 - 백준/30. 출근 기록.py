'''
[문제]
- 세명의 직원 A, B, C가 있다. 
- 하루에 한 명만 출근한다. AAC => 처음 이틀은 A가 출근, 셋째 날에 C가 출근
- A는 매일 매일 출근할 수 있다. B는 출근한 다음날은 반드시 쉬어야 한다. C는 출근한 다음날과 다다음날을 반드시 쉬어야 한다.
- 출근 기록 S가 주어졌을 때, S의 모든 순열 중에서 올바른 출근 기록인 것 아무거나 출력하라.
- 만약, 올바른 출근 기록이 없는 경우 -1을 출력하라.

[점화식]
- dp[a][b][c][전전날][전날] => a: A 출근 횟수, b: B 출근 횟수, c: C 출근 횟수, 전전날: 전전날 출근한 사람, 전날: 전날 출근한 사람


✅ 답 참고함, 다시 풀기
'''

def helper(a, b, c, prev):
    # 초기 A, B, C의 개수와 같다면, 올바른 출근 기록이므로 출력
    if [a, b, c] == cnt:
        print(''.join(perm))
        exit(0)
        
    # 이미 확인했던 것이면
    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    # 확인했음을 표시(= 방문 표시)
    dp[a][b][c][prev[0]][prev[1]] = 1
    
    # A 출근이 가능하면
    if a + 1 <= cnt[A]:
        perm[a + b + c] = 'A' 
        
        # A가 출근헀으므로 prev[0](전전날)에는 prev[1], prev[1](전날)은 A를 넣어준다.
        if helper(a + 1, b, c, [prev[1], A]):
            return True
        
    # B 출근이 가능하면
    if b + 1 <= cnt[B]:
        perm[a + b + c] = 'B'
        # 전날 출근하지 않았으면(쉬었다면)
        if prev[1] != B:
            if helper(a, b + 1, c, [prev[1], B]):
                return True
            
    # C 출근이 가능하면
    if c + 1 <= cnt[C]:
        perm[a + b + c] = 'C'
        # 전날, 전전날 모두 출근하지 않았다면(쉬었다면)
        if prev[0] != C and prev[1] != C:
            if helper(a, b, c + 1, [prev[1], C]):
                return True
            
    return False

s = input()
n = len(s)

perm = [''] * n # 정답을 저장할 배열
A, B, C = 0, 1, 2 # A: 0, B: 1, C: 2 -> cnt 배열 접근을 위해

cnt = [s.count(alp) for alp in ('A', 'B', 'C')] # A, B, C의 출근 횟수

# dp[a][b][c][전전날][전날] => a: A 출근 횟수, b: B 출근 횟수, c: C 출근 횟수, 전전날: 전전날 출근한 사람, 전날: 전날 출근한 사람
dp = [[[[[0] * 3 for _ in range(3)] for _ in range(n)] for _ in range(n)] for _ in range(n)]

# 수행
helper(0, 0, 0, [0, 0])

# 올바른 출근 기록이 없는 경우
print(-1)
