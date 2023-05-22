##  블로그에 자세한 설명 추가했습니다

def solution(target):
    # target까지 도달하는 데 필요한 최소 다트 수와 "싱글" 또는 "불"을 맞춘 횟수를 기록하는 배열
    # 최댓값으로 초기화
    dp = [[float('inf'), 0] for _ in range(300000)]

    # 가능한 과녁 값들
    targetList = [i + 1 for i in range(20)]

    # 시작 지점의 다트 수는 0으로 초기화
    dp[0][0] = 0

    # target까지 탐색
    for i in range(target):
        def updateDart(addIdx, count):
            # 던진 다트 수를 갱신할 필요가 있는 경우
            if dp[i + addIdx][0] >= dp[i][0] + 1:
                if dp[i + addIdx][0] == dp[i][0] + 1:
                    # 기존 값과 비교하여 "싱글" 또는 "불"을 맞춘 횟수(합) 갱신
                    dp[i + addIdx][1] = max(dp[i + addIdx][1], dp[i][1] + count)
                else:
                    # 던진 다트 수와 "싱글" 또는 "불"을 맞춘 횟수(합)을 갱신
                    dp[i + addIdx] = [dp[i][0] + 1, dp[i][1] + count]

        # 모든 과녁 값에 대해 확인
        for j in targetList:
            # 싱글, 더블, 트리플을 순서대로 적용하여 갱신
            for multiplier, hitCount in [[1, 1], [2, 0], [3, 0]]:
                updateDart(j * multiplier, hitCount)

        # "불"에 대해서도 확인하여 갱신
        updateDart(50, 1)

    # target까지 도달하는 데 필요한 최소 다트 수와 "싱글" 또는 "불"을 맞춘 횟수 반환
    return dp[target]