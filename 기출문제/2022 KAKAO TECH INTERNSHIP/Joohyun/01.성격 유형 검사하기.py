from sys import stdin,stdout

def solution(survey, choices):
    types = ['R','T','C','F','J','M','A','N']
    answer = {'R':0,'T':0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for sur,cho in zip(survey,choices):
        if sur=="RT" or sur=="TR":
            if cho<4:answer[sur[0]]+=4-cho
            else : answer[sur[1]]+=cho-4
        elif sur=="CF" or sur=="FC":
            if cho<4:answer[sur[0]]+=4-cho
            else : answer[sur[1]]+=cho-4
        elif sur=="JM" or sur=="MJ":
            if cho<4:answer[sur[0]]+=4-cho
            else : answer[sur[1]]+=cho-4
        else : # sur=="AN" or sur=="NA"
            if cho<4:answer[sur[0]]+=4-cho
            else : answer[sur[1]]+=cho-4

    result =[]
    for i in range(4):
        if answer[types[i*2]] >= answer[types[i*2+1]] : result.append(types[i*2])
        else : result.append(types[i*2+1])
    return ''.join(result)