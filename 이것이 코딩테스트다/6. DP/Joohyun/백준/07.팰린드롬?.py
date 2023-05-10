# 팰린드롬 : 앞 뒤를 뒤집어도 똑같은 문자열
import sys
input = sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))
m = int(input())
questions = [list(map(int,input().split())) for _ in range(m)]

dp = [[0]*n for _ in range(n)]

for num_len in range(n):
    for start in range(n-num_len):
        end = start+num_len
        
        if num_len==0 :                      # 문자열 길이가 1이면 -> 팰린드롬
            dp[start][end]=1
        elif numbers[start]==numbers[end] :  # 문자열 길이가 2 이상이고, 양 끝 문자가 같으면 
            if num_len<3:dp[start][end]=1       # 문자열 길이가 2 또는 3이면 -> 팰린드롬
            elif dp[start+1][end-1]==1 :        # 문자열 길이가 4 이상이고, 중간 문자열이 팰린드롬이면 -> 팰린드롬
                dp[start][end]=1
                
for s,e in questions:
    print(dp[s-1][e-1])