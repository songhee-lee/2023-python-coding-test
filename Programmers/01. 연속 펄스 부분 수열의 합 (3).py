def solution(sequence):
    answer = 0
    prefixS = [0]
    for i in range(len(sequence)):
        pulse = 1 if i % 2 == 0 else -1
        prefixS.append(prefixS[-1] + pulse * sequence[i])

    return abs(max(prefixS) - min(prefixS))
