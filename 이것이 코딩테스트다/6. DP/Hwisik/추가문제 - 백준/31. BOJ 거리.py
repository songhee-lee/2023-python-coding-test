'''
[문제]
- BOJ 거리 : 보도블록 N개가 일렬로 놓여진 형태의 도로
- 보도블록은 1번부터 N번까지 번호가 매겨져 있다.
- 스타트의 집은 1번에 있고, 링크의 집은 N번에 있다. 스타트는 링크를 만나기 위해서 점프하려고 한다.
- BOJ 거리의 각 보도블록에는 B, O, J 중 하나가 적혀있다. 1번은 반드시 B이다.
- 항상 번호가 증가하는 방향으로만 점프할 수 있다.
    - 만약, 스타트가 i번에 있다면, i + 1번부터 N번까지로 점프를 할 수 있다.
    - 한번 k칸 만큼 점프를 하는데 필요한 에너지의 양은 k * k이다.
- 스타트는 B,O,J,B,O,J,B,O,J, ... 순서로 보도블록을 밟으면서 점프를 할 것이다.
- 스타트가 링크를 만나기 위해 필요한 에너지의 최솟값을 구하시오.

[점화식]
- dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
    -> j번째에 도착하기 위해 i번째에서 점프를 했을 때, 필요한 에너지의 최솟값
    
'''
# 점프 규칙에 맞는 다음 문자 찾기
def find_next_step(cur):
    if cur == 'B':
        return 'O'
    if cur == 'O':
        return 'J'
    if cur == 'J':
        return 'B'
    
n = int(input())
_list = list(input())

# dp 테이블 초기화
dp = [float('inf')] * n
dp[0] = 0

# dp 테이블 갱신
# 스타트의 집에서 출발
for i in range(n):
    _next = find_next_step(_list[i]) # 다음으로 가야할 문자
    for j in range(i + 1, n):
        if _next == _list[j]:
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2) # 최소 에너지 값 갱신

print(dp[n - 1] if dp[n - 1] != float('inf') else -1)