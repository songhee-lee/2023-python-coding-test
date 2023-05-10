"""
n -> 1로 : n-1번 쪼개기
m -> 1로 : m-1번 쪼개기
 가로 먼저 쪼개면 세로는 가로 개수 배만큼 더 쪼개야함
 >> n-1 + (m-1)*n = n-1 + mn-n = mn-1
"""
from sys import stdin
input=stdin.readline
n,m=map(int,input().split())

print(m*n-1)