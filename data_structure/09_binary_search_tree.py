class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left  = Node(value)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        
        # 삭제 대상 노드 탐색
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        # 없으면 종료
        if not searched:
            return False

        # 1. Leaf Node삭제
        if not self.current_node.left and not self.current_node.right:
            if value > self.parent.value:
                self.parent.right = None
            else:
                self.parent.left = None

        # 2. Child Node가 하나인 Node삭제
        elif not self.current_node.left and self.current_node.right:
            if value > self.parent.value:
                self.parent.right = self.current_node.right
            else:
                self.parent.left = self.current_node.right
        elif self.current_node.left and not self.current_node.right:
            if value > self.parent.value:
                self.parent.right = self.current_node.left
            else:
                self.parent.left = self.current_node.left
        
        # 3. Child Node가 2개일때
        else:
            # 왼쪽자식
            if value < self.parent.value:
                self.changed_node = self.current_node.right
                self.changed_node_parent = self.current_node.right
                while self.changed_node.left:
                    self.changed_node_parent = self.changed_node
                    self.changed_node = self.changed_node.left
                # 옮기려는 노드의 오른쪽 노드가 존재할 때
                if self.changed_node.right:
                    self.changed_node_parent.left = self.changed_node.right
                else:
                    self.changed_node_parent.left = None
                # 옮기는 대상 삭제 됨, 이제 교체!
                self.parent.left = self.changed_node
                self.changed_node.right = self.current_node.right
                self.changed_node.left = self.current_node.left
            
            # 오른쪽 자식
            else:
                self.changed_node = self.current_node.right
                self.changed_node_parent = self.current_node.right
                while self.changed_node.left:
                    self.changed_node_parent = self.changed_node
                    self.changed_node = self.changed_node.left
                if self.changed_node.right:
                    self.changed_node_parent.left = self.changed_node.right
                else:
                    self.changed_node_parent.left = None
                self.parent.right = self.changed_node
                self.changed_node.right = self.current_node.right
                self.changed_node.left = self.current_node.left

        return True