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
        self.hash_table[hash_address] = value

    def read_data(self, data):
        hash_address = self.hash_function(self.get_key(data))
        return self.hash_table[hash_address]

hash_table = HashTable(8)
hash_table.save_data("윤정", "01045115625")
print(hash_table.read_data("윤정"))
# 01045115625

