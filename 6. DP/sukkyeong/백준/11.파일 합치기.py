'''
결국 시간초과 아직 해결 못함

파일의 크기를 입력 받고, 각 파일의 크기의 누적 합을 구합니다.
각 구간의 최소 비용을 저장할 2차원 리스트(dp)를 생성합니다.
구간 길이를 2부터 K까지 순서대로 계산합니다. (start와 end 변수로 구간을 나타냄)
구간을 나누어서 최소 비용 계산합니다. (mid 변수로 구간을 나눔)
구간의 최소 비용을 구하기 위해 dp[start][end]에 최소 값을 저장합니다.
전체 파일을 합치는 데 필요한 최소 비용인 dp[1][K]를 출력합니다.
'''


T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    K = int(input())  # 파일의 수
    file_sizes = list(map(int, input().split()))  # 각 파일의 크기
    sums = [0] * (K + 1)  # 파일 크기의 누적 합을 저장할 리스트

    for i in range(1, K + 1):
        sums[i] = sums[i - 1] + file_sizes[i - 1]  # 파일 크기의 누적 합 계산

    dp = [[0] * (K + 1) for _ in range(K + 1)]  # 각 구간의 최소 비용을 저장할 2차원 리스트

    # 구간 길이를 2부터 K까지 순서대로 계산
    for length in range(2, K + 1):
        for start in range(1, K - length + 2):
            end = start + length - 1
            dp[start][end] = float('inf')  # 구간의 최소 비용을 구하기 위해 최대 값으로 초기화

            # 구간을 나누어서 최소 비용 계산
            for mid in range(start, end):
                dp[start][end] = min(
                    dp[start][end], dp[start][mid] + dp[mid+1][end] + sums[end] - sums[start-1])

    print(dp[1][K])  # 전체 파일을 합치는 데 필요한 최소 비용 출력
