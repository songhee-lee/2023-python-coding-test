"""
해시나 배열을 이용하여 각 성격 유형별로 점수를 저장합니다.
해시나 조건문을 이용하여 각 설문지에서 선택한 대로 성격 유형에 점수를 부여합니다.
모든 문제에 대하여 각 성격 유형에 점수를 부여한 후, 적절한 for 문과 if 문으로 각 지표마다 어떤 성격 유형이 점수가 더 높은지 확인합니다.
점수가 같을 경우 사전순으로 빠른 성격 유형을 선택합니다.
"""


def solution(survey, choices):
    answer = ''

    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    mbti_add = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}

    for i in range(len(survey)):
        mbti[survey[i][0]] += mbti_add[choices[i]]
    answer += 'R' if mbti["R"] >= mbti["T"] else 'T'
    answer += 'C' if mbti["C"] >= mbti["F"] else 'F'
    answer += 'J' if mbti["J"] >= mbti["M"] else 'M'
    answer += 'A' if mbti["A"] >= mbti["N"] else 'N'
    return answer
