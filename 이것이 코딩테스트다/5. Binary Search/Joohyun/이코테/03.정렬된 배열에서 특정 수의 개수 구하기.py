n,x = map(int,input().split())
array = list(map(int,input().split()))
idx = []
visited = [[True] for _ in range(n)]

def binary_search_rec(array,target,start,end,idx,visited):
    if start>end : return None
    
    mid = (start+end)//2
    print(f'mid = {mid}')
    visited[mid] = False    # 방문 처리
    if array[mid]==target : 
        idx.append(mid)
        if visited[(start+mid-1)//2] : binary_search_rec(array,target,start,mid-1,idx,visited)
        if visited[(mid+1+end)//2] : binary_search_rec(array,target,mid+1,end,idx,visited)
    elif array[mid] > target : binary_search_rec(array,target,start,mid-1,idx,visited)
    else : binary_search_rec(array,target,mid+1,end,idx,visited)

binary_search_rec(array,x,0,n-1,idx,visited)
if idx : print(max(idx)-min(idx)+1)
else : print(-1)