def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)

    while start <= end:
        middle = (start + end)//2  # 중간값 계산

        max_count = 0  # 최대 연속된 돌의 개수
        count = 0  # 현재 연속된 돌의 개수
        flag = False  # 0의 시작 여부를 판단하는 플래그

        # stones 리스트 순회
        for stone in stones:
            if stone - middle <= 0:  # 돌의 값이 중간값 이하인 경우
                if flag:
                    count += 1  # 연속된 돌의 개수 증가
                else:
                    max_count = max(max_count, count)  # 이전의 최대 연속된 돌의 개수와 비교하여 갱신
                    count = 1  # 현재 연속된 돌의 개수 초기화
                    flag = True  # 0의 시작으로 플래그 변경
            else:
                flag = False  # 연속이 끝났으므로 플래그 변경

        max_count = max(max_count, count)  # 마지막 연속된 돌의 개수와 비교하여 갱신

        if max_count >= k:  # 최대 연속된 돌의 개수가 k보다 크거나 같은 경우
            end = middle - 1  # 중간값을 감소시켜서 더 작은 범위에서 탐색
            answer = middle  # 현재 중간값을 정답으로 저장
        else:
            start = middle + 1  # 중간값을 증가시켜서 더 큰 범위에서 탐색

    return answer