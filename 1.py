# 빈 스택(리스트) 초기화
stack = []
stack


# 스택에 원소 추가

stack = [1,2,3]
stack.append(4)

stack


# 스택에서 원소 제거

stack = [1,2,3]
top = stack.pop()

print(top)
stack


# 스택의 top 가져오기

stack = [1,2,3]
top = stack[-1]

top



# 스택의 이해하기 위한 예시 자료

# stack이란 리스트를 만든다.
stack = []

# 삽입(1) - 삽입(2) - 삽입(3) - 삭제 – 삽입(4)
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(4)

# stack 리스트 출력
print(stack)