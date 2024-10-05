n, m = map(int, input().split())  # 큐의 크기 n, 뽑아낼 원소의 개수 m
positions = list(map(int, input().split()))  # 뽑아낼 원소의 위치에 대한 리스트 생성

queue = list(range(1, n + 1))  # 큐 초기화(1부터 n까지)
moves = 0  # 총 이동 횟수 저장

for remove in positions :
    # 목표 원소의 현재 위치
    pos = queue.index(remove )
    
    # 왼쪽으로 이동할 때
    left = pos
    # 오른쪽으로 이동할 때 (전체 길이에서 현재 위치를 뺀 값)
    right = len(queue) - pos
    
    # 왼쪽과 오른쪽 중 더 적은 이동 횟수를 moves에 더함
    moves += min(left, right)
    
    # 원소를 큐에서 제거
    queue.pop(pos)

# 총 이동한 횟수 출력
print(moves)
