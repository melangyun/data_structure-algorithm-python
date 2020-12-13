queue_list = list()

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def desc(self):
        for i in range(len(self.queue)):
            print(self.queue[i])

queue = Queue()
for i in range(4):
    queue.enqueue(i)

queue.desc()
queue.dequeue()
queue.desc()
