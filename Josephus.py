# 1158. 요세푸스 문제

n,k = map(int, input().split())  # n은 사람 수, k는 제거할 순번

people = list(range(1, n+1))  # 사람 수를 1부터 n까지 리스트로 생성
result = []  # 제거된 사람들의 순서 리스트
index = 0  # 첫번째 사람의 인덱스

while people:  # 모든 사람이 제거될 때까지 계속 반복
    index = (index + k - 1) % len(people)  # 현재 인덱스에서 k번째 사람을 찾음 (% 연산 사용: 원형 리스트임을 고려)
    result.append(people.pop(index))  # 제거 후 결과 리스트에 추가

print("<", end="")  # "<" 먼저 출력
for i in range(len(result)):
    if i == len(result) - 1: 
        print(result[i], end="")     # 마지막 사람은 콤마 없이 출력
    else:  
        print(result[i], end=", ")    # 마지막 사람이 아닌 경우 콤마와 함께 출력
print(">")  # 마지막으로 ">" 출력
