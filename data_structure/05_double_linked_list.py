class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data, node)
            node.next = new
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def search_from_head(self, data):
        if not self.head:
            return False
        
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if not self.tail:
            return False
        
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev    
        return False

    def insert_before(self, data, before_data):
        if not self.head:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if not node:
                    return False
            new = Node(data, node.prev, node)
            node.prev.next = new
            node.prev = new
            if not new.prev:
                self.head = new
            return True

    def insert_after(self, data, after_data):
        if not self.head:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if not node:
                    return False
                new = Node(data, node, node.next)
                node.next = new
                new.next.prev = new

                if not new.next:
                    self.tail = new
                
                return True



    

            