""" 
1. 국어 점수 Reverse
2. 영어 점수 
3. 수학 점수 Reverse
4. 이름 사전순
"""

N = int(input())
students = []
for _ in range(N):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

students = sorted(students, key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(students[i][0])
