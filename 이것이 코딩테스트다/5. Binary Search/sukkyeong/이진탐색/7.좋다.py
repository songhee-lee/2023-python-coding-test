n = int(input())
nums = sorted(map(int, input().split()))

answer = 0


def two_pointer(li, target):
    global answer

    start, end = 0, len(li) - 1

    while start < end:
        s = li[start] + li[end]
        if target == s:
            answer += 1
            return
        elif target > s:
            start += 1
        elif target < s:
            end -= 1


for i in range(n):
    two_pointer(nums[:i] + nums[i+1:], nums[i])

print(answer)
