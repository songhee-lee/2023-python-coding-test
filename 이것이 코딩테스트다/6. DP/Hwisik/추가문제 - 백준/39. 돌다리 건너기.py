'''
[문제]
- 지나가야하는 다리는 두 개의 인접한 돌다리로 구성되어 있다. <악마의 돌다리>, <천사의 돌다리>이다.
- 두 돌다리의 길이는 항상 동일하며, 각 칸의 문자는 해당 돌에 새겨진 문자를 나타낸다.
- 두 다리에 새겨진 각 문자는 {R, I, N, G, S} 중 하나이다.
- 돌다리를 건너갈 때 반드시 순서대로 밟고 지나가야할 문자들이 적혀있다. 다음 조건을 만족해야 한다.
    1. 왼쪽(출발지역)에서 오른쪽(도착지역)으로 다리를 지나가야 하며, 반드시 마법의 두루마리에 적힌 문자열의 순서대로 모두 밟고 지나가야 한다.
    2. 반드시 <악마의 돌다리>와 <천사의 돌다리>를 번갈아가면서 돌을 밟아야 한다. 단, 출발은 어떤 돌다리에서 시작해도 된다.
    3. 반드시 한 칸 이상 오른쪽으로 전진해야하며, 건너뛰는 칸의 수는 상관이 없다.
- 이때, 돌다리를 통과할 수 있는 모든 가능한 방법의 수를 구하라.
[점화식]
- 

✅ 답 참고, 다시 풀기
'''

strings = input()
devil = input()
angel = input()
