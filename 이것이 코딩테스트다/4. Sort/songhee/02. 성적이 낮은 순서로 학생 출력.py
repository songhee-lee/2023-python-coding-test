""" 
- 성적이 낮은 순서대로 학생 이름 출력하기
"""

N = int(input())
q= []
for _ in range(N):
    name, score = input().split()
    q.append((name, int(score)))

print(*sorted(q, key=lambda x:x[1]))