n = int(input())
N = sorted(list(map(int,input().split())))
m = int(input())
M = sorted(list(map(int,input().split())))

print(f'가지고 있는 부품 : {N}')
print(f'필요한 부품 : {M}')

def binary_search_recur(array,target,start,end):
    print(f'현재 start = {start}, 현재 end = {end}')
    if start > end : return None

    mid = (start+end)//2
    print(f'mid = {mid}')
    
    if array[mid]==target : 
        print(f'array[{mid}]==target=={target}')
        return 'yes'
    elif array[mid]>target : binary_search_recur(array,target,start,mid-1)
    else : binary_search_recur(array,target,mid+1,end)


def binary_search_loop(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target: return 'yes'
        elif array[mid]>target: end=mid-1
        elif array[mid]<target: start=mid+1
    return None
    
print('재귀함수를 이용한 이진 탐색')
result = []
for target in M :
    r = binary_search_recur(N,target,0,n-1)
    print(r)
    if r == None : 
        result.append('no')
    else : result.append('yes')
print(*result)

print('반복문을 이용한 이진 탐색')
result = []
for target in M : 
    if binary_search_loop(N,target,0,n-1) == None : result.append('no')
    else : result.append('yes')
print(*result)