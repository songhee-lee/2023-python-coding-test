  attendences = [0] * 31

  for _ in range(28):
    num = int(input())
    attendences[num] = 1

  not_attend = []
  for i in range(1, 31):
    if not attendences[i]:
      not_attend.append(i)

  for i in range(2):
    print(not_attend[i])