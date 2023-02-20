import re
S = input()
S = re.sub('[0]{1,}','0',S)
S = re.sub('[1]{1,}','1',S)
print(min(S.count(S[0]),S.count(S[1])))
