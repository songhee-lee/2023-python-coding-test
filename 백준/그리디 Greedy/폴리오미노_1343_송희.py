string = input()
# 예외 처리
for s in string.split('.') :
    if len(s) % 2 == 1 :
        print("-1")
        exit()

prev = 0
answer = ''
for i, s in enumerate(string):
    if s == '.' :
        if i-prev == 2 :
            answer += "BB"
        else :
            answer += "AAAA" * ((i-prev) // 4) + "B" * ((i-prev)%4)
        answer += '.'
        prev = i+1

n = len(string)
if prev < n and string[prev] == 'X' and string[-1] == 'X' :
    answer += "AAAA" * ((n-prev) // 4) + "B" * ((n-prev)%4)

print(answer)