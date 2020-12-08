queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for i in range(10):
    enqueue(i)


print(len(queue_list))
# 10

print(dequeue())
# 0