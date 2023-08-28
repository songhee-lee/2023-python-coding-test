N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()	# 로프 정렬하기
answers = []	# 정답 배열

for rope in ropes :
    answers.append(rope * N)
    N -= 1

print(sorted(answers)[-1])
