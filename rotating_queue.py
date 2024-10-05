# 1021. 회전하는 큐

n, m = map(int, input().split())  # 큐의 크기 n, 뽑아내려고 하는 수의 개수 m
positions = list(map(int, input().split()))  # 뽑아내려고 하는 수가 저장된 리스트 생성

queue = list(range(1, n + 1))  # 큐 초기화(1부터 n까지)
moves = 0  # 총 이동 횟수를 저장

for remove in positions :
    # 뽑아내려고 하는 수의 현재 위치
    pos = queue.index(remove)
    
    # 왼쪽으로 이동하는 거리
    left = pos    # pos: 큐의 왼쪽에서의 이동 횟수
    # 오른쪽으로 이동하는 거리
    right = len(queue) - pos    # 큐의 총 길이에서 pos를 뺀 값
    
    # 왼쪽과 오른쪽 중 더 적은 이동 횟수를 moves에 더함
    moves += min(left, right)
    
    # 뽑아내려고 하는 수를 큐에서 제거
    queue.pop(pos)

print(moves)    # 총 이동 횟수를 출력
