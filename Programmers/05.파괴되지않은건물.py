'''자세한 설명은 블로그에 있습니다'''


def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    preSum = [[0] * (M + 1) for _ in range(N + 1)]  # 누적합 배열은 크기가 1 더 큼

    for s in skill:
        type = s[0]
        r1, c1, r2, c2, degree = s[1], s[2], s[3], s[4], s[5]

        if type == 1:  # 파괴할 때
            preSum[r1][c1] += -degree
            preSum[r2 + 1][c1] += degree
            preSum[r1][c2 + 1] += degree
            preSum[r2 + 1][c2 + 1] += -degree
        else:  # 회복 할 때
            preSum[r1][c1] += degree
            preSum[r2 + 1][c1] += -degree
            preSum[r1][c2 + 1] += -degree
            preSum[r2 + 1][c2 + 1] += degree

    # 가로 누적합 계산
    for i in range(N + 1):
        sum = 0
        for j in range(M + 1):
            sum += preSum[i][j]
            preSum[i][j] = sum

    # 세로 누적합 계산
    for i in range(M):
        sum = 0
        for j in range(N):
            sum += preSum[j][i]
            preSum[j][i] = sum

    # count
    for i in range(N):
        for j in range(M):
            if preSum[i][j] + board[i][j] > 0:
                answer += 1

    return answer