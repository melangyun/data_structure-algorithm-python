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
            if node.data[0] == data:
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
            # 만일 hash_table[n]에 있는게 없다면 새 링크드 리스트를 넣고 끝냄
            self.hash_table[hash_address] = LinkedList([data, value])
        else:
            node = linked_list.search(data)
            # 이미 존재하는 data라면, node가, 그렇지 않다면 False가 될것임
            if node:
                node.data[1] = value
            else:
                linked_list.add(value)

    def read_data(self, data):
        hash_address = self.hash_function(self.get_key(data))
        linked_list =  self.hash_table[hash_address]
        if not linked_list:
            # 만일 hash_table[n]에 있는게 없다면(0이라면) linkedList 를 찾아볼 필요 없이 종료
            return False
        node = linked_list.search(data)
        if not node:
            # node가 False라면 False 리턴 
            return False
        
        return node.data[1]

    def desc(self):
        print(self.hash_table)
        

hash_table = HashTable(10)
hash_table.save_data("김아무개", "01001928374")
hash_table.save_data("최윤정", "01098765432")
hash_table.save_data("김아무개", "01012345678")
hash_table.desc()
hash_table.save_data("최윤정", "01054677123")
print(hash_table.read_data("윤정"))
# False
print(hash_table.read_data("김아무개"))
# 01012345678
print(hash_table.read_data("최윤정"))
# 01054677123
