# Stack

# 주요 용어
# Lifo
# push, pop
# peak -> 스택의 변형 없이 맨 위의 값을 출력

# 장점
# 구조가 단순, 구현이 쉬움
# 데이터의 저장/읽기 속도가 빠름

# 단점
# 데이터의 최대 갯수를 미리 정해야 한다. (파이썬의 경우 1000개 최대)
# 저장 공간의 낭비

# 사용
# 컴퓨터 내부의 프로세스 구조의 함수 동작방식 
# ㄴ 계속 까먹으면 아래 재귀함수 호출시 스택이 쌓이는 구조를 다시 생각해보기

def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data -1)
        print("returned", data)

recursive(4)
# 4
# 3
# 2
# 1
# 0
# ended
# returned 0
# returned 1
# returned 2
# returned 3
# returned 4

# python list 활용한 구현

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()
    def peak(self):
        return self.items[-1]
    def isEmpty(self):
        # python 에서는 배열이 비어있다면 false!
        return not self.items

stack = Stack()
print(stack)
print(stack.isEmpty()) # True
stack.push(1)
stack.push(2)
print(stack.peak())
print(stack.pop())
print(stack.isEmpty()) # False
