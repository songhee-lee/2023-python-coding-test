#자세한 풀이는 개인 블로그에 업로드하였습니다

def solution(e, starts):
    answer = []
    multiples = [0] * (e + 1)  # 수의 등장 횟수를 기록할 리스트 초기화

    # 배수 세기
    for i in range(1, int(e ** 0.5) + 1):  # 제곱근까지만 반복
        for j in range(i, e // i + 1):  # i 이상 e // i 이하의 수들을 반복
            multiple = i * j  # 배수 계산
            multiples[multiple] += (2 if i != j else 1)  # 중복되지 않는 경우 2를 더하고, 중복되는 경우 1을 더함

    counts = [0] * (e + 1)  # 등장 횟수에 따른 숫자 기록할 리스트 초기화
    max_count = 0

    # 약수의 개수가 큰 순서대로 정렬
    for idx in range(e, 0, -1):  # e부터 1까지 역순으로 반복
        if multiples[idx] >= max_count:
            max_count = multiples[idx]
            counts[idx] = idx
        else:
            counts[idx] = counts[idx + 1]  # 등장 횟수가 이전 값보다 작으면 이전 값으로 갱신

    # 답 목록 구하기
    for start in starts:
        answer.append(counts[start])

    return answer