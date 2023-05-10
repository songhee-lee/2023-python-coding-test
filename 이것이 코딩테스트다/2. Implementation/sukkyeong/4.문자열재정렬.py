s = input()

str_list = []
num_sum = 0

for i in s:
    if i.isalpha():
        str_list.append(i)
    elif i.isdigit():
        num_sum += int(i)

str_list.sort()

result = ''.join(str_list) + str(num_sum)
print(result)
