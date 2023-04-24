'''
어피치가 화살 n발을 쏘고 라이언이 화살 n발을 쏨
가장 작은 원의 점수는 10점이고 가장 큰 원의 바깥쪽은 과녁 점수가 0점
동점이면 신규, 아니면 더 많이 맞춘 사람이 k점 점수를 가져감
어피치가 다 쏜 상황, 라이언이 쏠 상황
n발의 화살을 어디에 맞혀야 하는지를 구하기
무조건 비기는 경우는 -1을 리턴하기

score 함수는 라이언이 얻은 점수를 계산
라이언이 해당 종류의 과녁에서 얻은 점수가 더 높은 경우에는 (10-i)점을 더하고, 그렇지 않은 경우에는 (10-i)점을 빼기
dfs 함수는 백트래킹 기법을 사용하여 가능한 모든 라이언의 화살 개수 조합을 생성
가능한 조합이 완성되면 score 함수를 호출하여 라이언의 점수를 계산하고, 최고 점수를 가지는 조합을 선택
answer 리스트에는 최고 점수를 가지는 조합이 저장되고, result 변수에는 그 때의 점수가 저장


'''
def solution(n, info):
    global best_archery, best_score

    # 라이언이 해당 종류의 과녁에서 얻은 점수를 계산하는 함수
    def calculate_score(archery):
        score = 0
        for i in range(11):
            if archery[i] == info[i] == 0:
                continue
            if archery[i] > info[i]:
                score += 10 - i
            else:
                score -= 10 - i
        return score

    # 백트래킹으로 가능한 모든 라이언의 화살 개수 조합을 생성하는 함수
    def dfs(idx, arrows_left, archery):
        global best_archery, best_score
        if idx == -1 and arrows_left:
            return
        if arrows_left == 0:
            score = calculate_score(archery)
            if best_score < score:
                best_archery = archery[:]
                best_score = score
            return
        for i in range(arrows_left, -1, -1):
            archery[idx] = i
            dfs(idx-1, arrows_left-i, archery)
            archery[idx] = 0

    # 최고 점수를 가지는 조합을 찾기 위한 초기화
    best_archery = [0 for _ in range(11)]
    best_score = 0

    # dfs 함수 호출
    dfs(10, n, [0 for _ in range(11)])

    # 결과 반환
    return best_archery if best_score != 0 else [-1]
