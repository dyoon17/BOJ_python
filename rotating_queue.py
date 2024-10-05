n, m = map(int, input().split())  # 큐의 크기 n, 뽑아낼 원소의 개수 m
targets = list(map(int, input().split()))  # 뽑아낼 원소의 위치

queue = list(range(1, n + 1))  # 큐 초기화
moves = 0  # 이동 횟수 저장

for target in targets:
    # 목표 원소의 현재 위치
    pos = queue.index(target)
    
    # 왼쪽으로 이동할 때와 오른쪽으로 이동할 때 중 더 적은 이동 횟수를 선택
    left = pos
    right = len(queue) - pos
    
    # 더 적은 이동 횟수를 moves에 더함
    moves += min(left, right)
    
    # 원소를 제거
    queue.pop(pos)

# 총 이동한 횟수 출력
print(moves)
