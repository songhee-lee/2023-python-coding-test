from sys import stdin
input = stdin.readline

n,k=map(int,input().split())
arrA = [a for a in map(int,input().split())]
arrB = [b for b in map(int,input().split())]

"""
K 번 바꿔치기
arrA에서 가장 작은 원소 a
arrB에서 가장 큰 원소 b
a가 b보다 작으면 바꿔치기
"""
arrA.sort()
arrB.sort(reverse=True)
for i in range(k):
    if arrA[i] < arrB[i]: arrA[i],arrB[i]=arrB[i],arrA[i]
    else : break

print(sum(arrA))
