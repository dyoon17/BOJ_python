from collections import deque  

n = int(input())    # 보드의 크기 n
k = int(input())    # 사과의 개수 k

# 보드 생성
board = []  # 빈 보드를 리스트로 생성
for _ in range(n):  # 변수가 없지만 작업을 n번 반복한다는 뜻
    row = [0] * n  # 각 행을 n개의 0으로 채움
    board.append(row)  # 행들을 보드에 추가

# 사과의 위치
for _ in range(k):  # 사과의 개수 k만큼 반복한다는 뜻
    x, y = map(int, input().split())  # x는 행, y는 열로 사과의 위치 입력
    board[x - 1][y - 1] = 1  # 1부터 시작하는 좌표를 0부터 시작하는 인덱스에 맞추기 위해 -1 처리한 후..
# 사과가 있는 칸은 1로 바꿈

# 방향 전환 정보 입력
l = int(input())  # 뱀이 방향을 전환할 횟수 l
directions_info = []  # 방향 전환 정보를 저장할 리스트 (시간, 방향)
for _ in range(l):  # 방향 전환 횟수 l만큼 반복
    x, c = input().split()  # x는 시간, c는 방향 (L: 왼쪽으로 90도 회전, D: 오른쪽으로 90도 회전)
    directions_info.append((int(x), c))  # x는 정수형, c는 문자 그대로 저장(백준 입력창 참고)

# 방향 설정: (행, 열)로 표시
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 이동 방향: 오른쪽, 아래, 왼쪽, 위 순서
current_direction = 0  # 처음에는 오른쪽으로 이동하므로..

# 뱀의 초기 상태
snake = deque([(0, 0)])  # 뱀의 몸: 처음에 (0, 0)에 위치
time = 0  # 경과 시간
direction_index = 0  # 방향 전환 리스트에서 사용할 인덱스

# 게임 시작(끝날 때까지 루프 반복함)
while True:
    time += 1  # 1초씩 시간 증가

    head_x, head_y = snake[0]  # 뱀의 현재 머리 위치(머리의 x좌표는 행, 머리의 y좌표는 열)
    new_x = head_x + directions[current_direction][0]  # 새로운 머리의 x좌표
    new_y = head_y + directions[current_direction][1]  # 새로운 머리의 y좌표

    if not (0 <= new_x < n and 0 <= new_y < n) or (new_x, new_y) in snake:  # 새로운 좌표가 보드 안에 위치해야 함
        break      # 만약 벽이나 자신의 몸과 부딪히면 게임 종료

    snake.appendleft((new_x, new_y))  # 덱 앞에 좌표를 추가: 뱀의 머리 위치 갱신

    if board[new_x][new_y] == 1:  # 이동한 위치에 사과가 있을 때
        board[new_x][new_y] = 0  # 사과를 먹으면 보드에서 사과가 없어짐
    else:
        snake.pop()  # 사과가 없으면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌

    # 방향 전환 처리: 방향 전환의 처음 저장 수가 현재 처리 횟수보다 클 때(남은 처리 횟수가 있을 때)와...
    if direction_index < len(directions_info) and time == directions_info[direction_index][0]:  # 현재 시간이 방향 바꿀 시간과 같을 때(방향을 바꿀 시간이 되었을 때)
        turn = directions_info[direction_index][1]  # 현재 방향 전환 정보('L' 또는 'D')
        # 뱀이 왼쪽으로 회전할지, 오른쪽으로 회전할지를 결정함
        if turn == 'L':  # 왼쪽으로 90도 회전
            current_direction = (current_direction - 1) % 4  # % 4 연산: 숫자가 0~3 사이에서 순환-> directions 리스트 참고해서 방향 확인
        else:  # 오른쪽으로 90도 회전
            current_direction = (current_direction + 1) % 4
        direction_index += 1  # 다음 방향 전환해야 하므로 현재 처리 횟수 업데이트

# 게임 종료: 종료된 시간(초) 출력
print(time)
