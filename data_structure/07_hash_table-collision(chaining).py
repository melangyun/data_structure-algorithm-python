class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def delete(self, data):
        if self.head.data == "":
            return

        node = self.head
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def search(self, data):
        if not self.head:
            return False
        
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False


class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for i in range(self.size)]
    
    def get_key(self, data):
        return hash(data)
    
    def hash_function(self, key):
        return key % self.size

    def save_data(self, data, value):
        hash_address = self.hash_function(self.get_key(data))
        linked_list = self.hash_table[hash_address]
        if not linked_list:
            self.hash_table[hash_address] = LinkedList(value)
        else:
            linked_list.add(value)

    def read_data(self, data, value):
        hash_address = self.hash_function(self.get_key(data))
        linked_list =  self.hash_table[hash_address]
        node = linked_list.search(value)
        return node.data

    def desc(self):
        print(self.hash_table)
        

hash_table = HashTable(2)
hash_table.save_data("윤정", "01045115625")
hash_table.desc()
print(hash_table.read_data("윤정","01045115625"))
# 01045115625

