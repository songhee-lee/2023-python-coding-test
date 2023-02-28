from itertools import permutations
N = int(input()) # N : 수의 개수
A = list(map(int,input().split()))  # A : 수열
pmmd = list(map(int,input().split())) # 연산자 개수 : 덧셈, 뺄셈, 곱셈, 나눗셈 순
op = ['+', '-', '*', '//'] # 연산 종류

# ops : 연산자 종류별로 개수만큼 나열
ops = []
for i in range(4):
    if pmmd[i]:
        ops.append(op[i]*pmmd[i])
ops = list(''.join(ops))

# 연산자 순서 리스트, 순열+중복제거
OPS = set(list(permutations(ops,len(ops))))

Result = [] # 모든 연산 결과들의 리스트
for o in OPS:
    o = list(o) # 연산자 순서 (차례대로)
    result = A[0] 
    # 연산자 순서대로 연산하기
    for i in range(N-1):
        if o[i] == '+' :result+=A[i+1]
        elif o[i] == '-' : result-=A[i+1]
        elif o[i] == '*' : result*=A[i+1]
        elif o[i] == '//' : 
            if result < 0 :
                result = result*-1//A[i+1]*-1
            else : result//=A[i+1]
    Result.append(result)

print(max(Result))
print(min(Result))