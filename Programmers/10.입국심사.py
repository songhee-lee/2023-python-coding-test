def solution(n, times):
    left, right = 1, max(times) * n  # 이분 탐색을 위한 범위 설정. 최솟값은 1, 최댓값은 가장 오래 걸리는 심사관이 모두 심사하는 경우
    answer = right  # 최종 결과값을 저장할 변수. 초기에는 최댓값으로 설정

    while left <= right:  # 이분 탐색을 진행하는 반복문. 왼쪽 범위가 오른쪽 범위를 넘어갈 때까지 반복
        mid = (left + right) // 2  # 현재 범위의 중간값
        people = sum(mid // time for time in times)  # 중간값을 각 심사관이 걸리는 시간으로 나누어 심사를 마친 사람의 수를 계산

        if people >= n:  # 심사를 마친 사람의 수가 n 이상인 경우
            answer = min(answer, mid)  # 현재까지의 최소 시간을 갱신
            right = mid - 1  # 오른쪽 범위를 줄여서 더 작은 시간을 탐색
        else:
            left = mid + 1  # 왼쪽 범위를 늘려서 더 큰 시간을 탐색

    return answer  # 최소 시간을 반환
