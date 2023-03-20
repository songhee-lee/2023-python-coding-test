import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ab, cd = [], []
    for i in range(n):
        for j in range(n):
            ab.append(arr[i][0] + arr[j][1])
            cd.append(arr[i][2] + arr[j][3])

    ab.sort()
    cd.sort()
    # print(ab, cd)
    i, j = 0, len(cd) - 1  # i는 ab의 시작점, j는 cd의 끝점(투포인터)
    result = 0
    while i < len(ab) and j >= 0:
        if ab[i] + cd[j] == 0:  # 합이 0이 되는 경우
            nexti, nextj = i + 1, j - 1
            # ab가 같은게 여러개인경우
            while nexti < len(ab) and ab[i] == ab[nexti]:
                nexti += 1
            # cd가 같은게 여러개인경우
            while nextj >= 0 and cd[j] == cd[nextj]:
                nextj -= 1

            result += (nexti - i) * (j - nextj)  # 이야... 지리네
            i, j = nexti, nextj

        elif ab[i] + cd[j] > 0:  # cd가 ab보다 더 절댓값이 큰경우
            j -= 1
        else:  # ab가 cd보다 더 절댓값이 큰 경우
            i += 1

    print(result)
