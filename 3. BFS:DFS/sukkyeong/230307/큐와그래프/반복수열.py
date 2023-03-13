a, p = map(int, input().split())

nums = [a]
while True:
    tmp = 0
    for s in str(nums[-1]):
        tmp += int(s) ** p
    if tmp in nums:
        break

    nums.append(tmp)
print(nums.index(tmp))
