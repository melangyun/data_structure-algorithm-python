class HashTable:
    def __init__(self, table_size):
        self.size = table_size
        self.hash_table = [0 for i in range(self.size)]
    
    def get_key(self, data):
        return hash(data)
    
    def hash_function(self, key):
        return key % self.size

    def save_data(self, data, value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        if not self.hash_table[hash_address]:
            for i in range (hash_address, self.size):
                if self.hash_table[i] == 0:
                    self.hash_table[i] = [index_key, value]
                    return
                elif self.hash_table[i][0] == index_key:
                    self.hash_table[i][1] = value #업데이트
        else:
            self.hash_table[hash_address] = [index_key, value]

    def read_data(self, data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)

        if self.hash_table[hash_address] != 0:
            for i in range(index_key, self.size):
                if self.hash_table[i] == 0:
                    return None
                elif self.hash_table[i][0] == index_key:
                    return self.hash_table[i][1]
        else:
            return None
