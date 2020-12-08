# 주요 용어
# Enqueue : 데이터를 넣음
# Dequeue : 데이터를 꺼냄

# 특징
# FIFO, 혹은 LILO
# ? 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 사용됨

import queue

queue_data = queue.Queue()
# enqueue
queue_data.put(1)
queue_data.put(2)

# size
queue_size = queue_data.qsize()
print(queue_size) # 2

# dequeue
firstoutput = queue_data.get()
print(firstoutput) # 1


# ! LifoQueue
lifo_queue = queue.LifoQueue()
# 이외 사용법 동일

# ! PriorityQueue : 우선순위 queue
priority_queue = queue.PriorityQueue()
# 데이터가 일종의 튜플 단위로 들어감.  우선순위가 높은것이 숫자가 낮음
priority_queue.put((10, "rice"))
priority_queue.put((4, "pizza"))
priority_queue.put((7, "chicken"))

foremost_data = priority_queue.get()
print(foremost_data)
# (4, 'pizza')