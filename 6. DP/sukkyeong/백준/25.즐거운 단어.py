def solve(f, i, j, k):
    # 현재 _ 개수가 3개 이상이거나 L 개수가 3개 이상이면 경우의 수가 존재하지 않음
    if i >= 3 or j >= 3:
        return 0

    # 모든 글자를 다 채웠으면 경우의 수 1개를 찾음
    if k == n:
        return f

    # 이미 구한 경우의 수인 경우 그대로 반환
    if dp[f][i][j][k] != -1:
        return dp[f][i][j][k]

    ret = 0

    # 현재 글자가 _ 일 경우
    if arr[k] == '_':
        # 다음 글자가 자음일 때의 경우의 수
        ret += solve(f, i+1, 0, k+1) * 5
        # 다음 글자가 모음일 때의 경우의 수
        ret += solve(f, 0, j+1, k+1) * 20
        # 다음 글자가 L 일 때의 경우의 수
        ret += solve(1, 0, j+1, k+1)
    # 현재 글자가 모음일 경우
    elif arr[k] in vow:
        ret = solve(f, i+1, 0, k+1)
    # 현재 글자가 L 일 경우
    elif arr[k] == 'L':
        ret = solve(1, 0, j+1, k+1)
    # 현재 글자가 자음일 경우
    else:
        ret = solve(f, 0, j+1, k+1)

    # 현재 경우의 수를 dp 배열에 저장
    dp[f][i][j][k] = ret
    return ret


# 입력받은 문자열
arr = input()
# 문자열의 길이
n = len(arr)
# dp 배열
dp = [[[[-1] * (n+1) for i in range(4)] for j in range(4)] for k in range(2)]
# 모음을 저장한 집합
vow = {'A', 'E', 'I', 'O', 'U'}

# solve 함수 호출 후 결과 출력
print(solve(0, 0, 0, 0))
