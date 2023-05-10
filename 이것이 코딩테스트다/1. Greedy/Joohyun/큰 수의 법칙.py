N, M, K = map(int,input().split())
Nums = sorted(list(map(int,input().split())), reverse=True)

q, r = divmod(M,K+1)
print((K*q+r)*Nums[0]+q*Nums[1])
