def solution(s):
    answer = len(s)  # 최소 길이를 s의 길이로 초기화

    # 문자열을 자를 단위를 1~ len(s)까지 반복
    for i in range(1, len(s)):
        unit = i  # 자르는 단위
        compressed = ""  # 압축한 문자열
        prev = s[0:unit]  # 이전에 자른문자열, 초기값은 첫 단위로 자른 문자열

        count = 1  # 현재 문자열의 개수를 카운트하는 변수
        for j in range(unit, len(s), unit):  # 단위(unit)만큼 문자열을 자르면서 반복
            current = s[j:j+unit]  # 현재 자른 문자열
            if prev == current:  # 현재 문자열이 이전 문자열과 같으면 count 증가
                count += 1
            else:  # 현재 문자열이 이전 문자열과 다르면 압축하여 compressed에 추가
                if count == 1:
                    compressed += prev
                else:
                    compressed += str(count) + prev
                prev = current  # 이전 문자열을 현재 문자열로 업데이트
                count = 1  # count를 1로 초기화

        # 마지막 문자열 처리
        if count == 1:
            compressed += prev
        else:
            compressed += str(count) + prev

        # 압축한 문자열의 길이를 갱신
        answer = min(answer, len(compressed))

    return answer
