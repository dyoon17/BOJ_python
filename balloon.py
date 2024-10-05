# 2346. 풍선 터뜨리기

from collections import deque

n, papers = int(input()), list(map(int, input().split()))  # 풍선의 개수와 종이에 적힌 수

# 풍선 번호와 종이에 적힌 수를 리스트로 저장
balloons = [(i + 1, papers[i]) for i in range(n)]  # 1번부터 n번까지 번호를 부여

result = []  # 풍선이 터진 순서를 저장할 결과 리스트
index = 0  # 현재 터뜨릴 풍선의 인덱스

while balloons:
    idx, move = balloons.pop(index)  # 현재 인덱스에 있는 풍선을 터뜨리고 그 번호와 이동할 값을 가져옴
    result.append(idx)  # 터진 풍선 번호를 결과 리스트에 추가

    if balloons:  # 남은 풍선이 있는지 확인한 후 이동을 계산
        if move > 0:  # 풍선에 적힌 숫자가 양수일 때
            index = (index + (move - 1)) % len(balloons)  # 오른쪽으로 이동(이미 터진 풍선 제외하고)
        else:
            index = (index + move) % len(balloons)  # 왼쪽으로 이동(이미 터진 풍선 제외하고)

for i in range(len(result)):
    if i == len(result) - 1:  # 마지막 요소에는 공백을 추가하지 않음
        print(result[i])
    else:
        print(result[i], end=" ")  # 마지막 요소가 아니면 공백과 함께 출력
