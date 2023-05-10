def solution(N,stages):
    k=len(stages)
    s=[]
    for i in range(1,N+1):
        c = 0
        for j in range(len(stages)):
            if stages[j]==i:c+=1
        if c==0: s.append(0)
        else: s.append(c/k)
        k=k-c
    a=sorted(s,reserved=True)
    answer =[]

    for i in range(len(a)):
        answer.append(s.index(a[i]+1))
        s[s.index(a[i])]=2
    return answer