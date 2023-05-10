from sys import stdin
input = stdin.readline
n = int(input())

students = [input().split() for i in range(n)]
students = sorted(students,key=lambda students:students[1])
for student in students:
    print(student[0], end=' ')