n,k = map(int, input().split())  # n과 k를 입력받아 각각 정수로 변환

people = list(range(1, n+1))  # 1부터 n까지의 숫자를 리스트로 생성 (사람들을 나타냄)
result = []  # 제거된 사람들의 순서를 담을 리스트 (최종적인 요세푸스 순열)
index = 0  # 처음 시작할 때 제거할 사람의 인덱스 (0번째부터 시작..)

while people:  # 리스트가 비어있지 않은 동안 계속 반복
    index = (index + k - 1) % len(people)  # 현재 인덱스에서 k번째 사람을 찾음 (원형임을 고려)
    result.append(people.pop(index))  # 찾은 사람을 리스트에서 제거하고 결과 리스트에 추가

# 출력
print("<", end="")  # 출력 형식에 맞게 "<" 먼저 출력
for i in range(len(result)):  # 결과 리스트를 하나씩 출력
    if i == len(result) - 1:  # 마지막 사람은 콤마 없이 출력
        print(result[i], end="")
    else:  # 마지막이 아닌 경우, 콤마와 함께 출력
        print(result[i], end=", ")
print(">")  # 마지막으로 ">"를 출력해서 마무리
