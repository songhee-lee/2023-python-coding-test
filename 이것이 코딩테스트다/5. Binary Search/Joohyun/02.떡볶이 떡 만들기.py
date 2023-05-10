n,m = map(int,input().split())
riceCakes = list(map(int,input().split()))
height = list(range(1,riceCakes[-1]+1))
answer = []

def binary_search_rec(height,target,start,end,answer):
    if start > end : return None

    # 절단기 높이 설정
    mid = (start+end)//2
    h = height[mid]

    # 떡 높이 총합
    riceSum = 0
    for riceCake in riceCakes:
        rc = riceCake-h
        rc = rc if rc > 0 else 0
        riceSum+=rc
    if riceSum == target : 
        print(h)
        exit(0)
    elif riceSum > target : 
        answer.append(h)
        binary_search_rec(height, target, mid+1,end,answer)
    else : binary_search_rec(height, target, start, mid-1,answer)

binary_search_rec(height,m,0,riceCakes[-1]-1,answer)
print(max(answer))