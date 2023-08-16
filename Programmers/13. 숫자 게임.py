# B에서 순서를 정할 때, 무조건 큰 점수부터 내보내면 안됨.
# A의 순서와 비교했을 때, 점수 차이가 최대한 적으면서 A팀의 점수보다 큰 순서로 내보내야 함.
# e.g. A팀의 첫 번쨰가 5점일 때, B팀은 6, 7이 있을 때 6을 내보내야 함.(차이가 1로 가장 적기 때문)
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    i, j = 0, 0
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
    return answer