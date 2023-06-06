def solution(s):
    answer = []
    for string in s:
        count, idx, stack, n = 0, 0, "", len(string)

        # 110 찾기
        for idx in range(n):          
            if string[idx] == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                count += 1
            else:
                stack += string[idx]

        idx = stack.find("111")             # 110이 빠진 string에서 111 찾기
        if idx == -1:                       # 0뒤에 110 반복해 붙이기
            idx = stack.rfind('0')
            stack = stack[:idx+1]+"110"*count+stack[idx+1:]
        else:                               # 111앞에 110 반복해 붙이기
            stack = stack[:idx]+"110"*count+stack[idx:]
        answer.append(stack)
    return answer