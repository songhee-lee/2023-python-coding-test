"""
<< 명령 >>
1. push X : 정수 X를 큐에 넣기
2. pop : 가장 앞에 있는 정수 빼서 출력 | 정수가 없으면 -1 출력
3. size : 정수 개수
4. empty : 비어있으면 1, 아니면 0
5. front : 가장 앞에 있는 정수 출력 | 정수 없으면 -1 출력
6. back : 가장 뒤에 있는 정수 출력 | 정수 없으면 -1 출력
"""

"""
< 입력 >
n : 명령 수 ( 1 <= n <= 10,000 )
1 <= 주어지는 정수 <= 100,000

< 출력 >
출력해야 하는 명령이 주어질 때마다 한 줄에 하나씩 출력
"""

# import sys
# from collections import deque

# n = int(input())
# cmds = ['push','pop','size','empty','front','back']
# result = deque()
# for i in range(n):
#     cmd = list(sys.stdin.readline().split())
#     idx = cmds.index(cmd[0])
#     if idx == 0: result.append(cmd[1])  # push x
#     if idx == 1:                        # pop
#         if result : print(result.popleft())
#         else : print(-1)
#     if idx == 2: print(len(result))     # size
#     if idx == 3:                        # empty
#         if result : print(0)
#         else : print(1)
#     if idx == 4:                        # front
#         if result:print(result[0])
#         else:print(-1)
#     if idx == 5:                        # back
#         if result:print(result[-1])
#         else:print(-1)


from sys import stdin,stdout

input = stdin.readline
print = stdout.write

print(1)
q = []

for _ in range(int(input())):
	cmd = input().rstrip()

	if cmd=="pop" : print(q.pop(0)+'\n') if q else print('-1\n')
	elif cmd=="size" : print(str(len(q))+'\n')
	elif cmd=="empty" : print('0\n') if q else print('1\n')
	elif cmd=="front" : print(q[0]+'\n') if q else print('-1\n')
	elif cmd=="back" : print(q[-1]+'\n') if q else print('-1\n')
	else: q.append(cmd.split()[1]) # push1

