'''
numbers : 이진트리로 만들고 싶은 수를 담은 1차원 정수 배열
numbers에 주어진 순서대로 하나의 이진트리로 해당 수를 표현할 수 있다면 1
없다면 0을 1차원 정수 배열에 담아 return
'''
#완전한 이진트리일 경우, 2진법 자리수 1개, 3개, 7개, 15개, 31개, 63개
#                    1, (1*2)+1, (3*2)+1, (7*2)+1, (15*2)+1, (31*2)+1 ... 
# (2**n)-1 

def check(tree):
    root = len(tree) // 2

    if root == 0:
        return True
    
    if tree[root] == '0' :
        if '1' not in tree:
            return True
        return False
    
    return check(tree[0:root]) and check(tree[root+1:])



def solution(numbers):
    answer = []

    for num in numbers:
        # 이진수만들기
        two = bin(num)[2:]
        
        # 포화이진트리 만들기
        nodes = bin(len(two) + 1)[2:]

        # 포화이진트리가 아닌 경우 0 추가
        # len(nodes) + 1 = 2^n 
        # 2^n은 첫자리가 1이고 나머지 0 으로 되어있음
        if '1' in nodes[1:]:  
            # 1<<len(nodes) : 자릿수+1 만큼 첫자리가 1이고 나머지 0으로 만듬
            # int(nodes,2) : nodes가 str 이어서 2진수로 만들어서 빼기 계산
            dummies = (1 << len(nodes)) - int(nodes, 2)
            two = '0' * dummies + two

        result = check(two)
        if result == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer
