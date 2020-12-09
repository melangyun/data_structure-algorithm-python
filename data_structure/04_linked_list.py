# 기본 구조와 용어
# 노드 (node) : 데이터 저장 단위(데이터값, 포인터)
# 포인터(pointer): 주소값이 존재

# 장점
# 데이터 공간을 미리 할당하지 않아도 됨 (배열은 미리 할당 필요)
# 단점
# 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
# 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
# 중간 데이터 삭제시, 앞 뒤 데이터의 연결을 재구성 해야하는 부가적인 작업 필요

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.header = Node(data)

    def add(self, data):
        if not self.header:
            self.header = Node(data)
        else:
            node = self.header
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        if self.header.data == "":
            print("노드가 없습니다")
            return

        if self.header.data == data:
            temp = self.header
            self.header = self.header.next
            del temp
        else:
                node = self.header
                while node.next:
                    if node.next.data == data:
                        temp = node.next
                        node.next = node.next.next
                        del temp
                        return
                    else:
                         node = node.next

    def desc(self):
        node = self.header
        while node:
            print(node.data)
            node = node.next
            

linkedList = NodeMgmt(0)
for i in range(1, 10):
    linkedList.add(i)

linkedList.delete(0)
linkedList.desc()