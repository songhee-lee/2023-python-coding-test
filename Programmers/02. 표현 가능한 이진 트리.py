def check(bin_num):
    root = len(bin_num)//2      # 중심 노드 위치
    if root == 0 :              # 길이가 1인 문자열은 리턴 (리프 노드)
        return True
    # 중심 노드가 0이면 자식 노드가 모두 0이어야 함
    if bin_num[root] == '0' :   
        if '1' not in bin_num:  
            return True
        return False
    
    # 왼쪽 / 오른쪽 자식 확인하기
    return check(bin_num[:root]) and check(bin_num[root+1:])


def solution(numbers):
    answer = []
    cbts = [1, 3, 7, 15, 31, 63]
    for number in numbers:
        bin_num = str(bin(number))[2:]  # 이진수
        length = len(bin_num)           # 이진수의 길이

        for cbt in cbts :
            if length == cbt :          # 완전 포화 트리 길이인 경우
                break
            elif length < cbt :         # 완전 포화 트리 길이로 만들기
                bin_num = "0"*(cbt-length) + bin_num
                length = cbt
                break
        answer.append(1 if check(bin_num) else 0 )

    return answer
