'''
학생 정보 =  학생의 이름, 성적
성적이 낮은 순서로 이름 출력
'''


n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append(data[0], int(data[1]))

array = sorted(array, key=lambda score: score[1])

for score in array:
    print(score[0], end=' ')
