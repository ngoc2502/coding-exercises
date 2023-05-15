class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    
class LinkedList(object):
    def __init__(self):
        self.tail = self.head = None       

    def insert(self,value):
        node = Node(value)

        if not self.head :
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
    
    def find(self, cur, prev, value):
        while cur:
            if cur.value == value:
                return cur, prev, True            
            cur = cur.next
            prev = cur
        return cur, prev, False
        
    
    def delete(self, value):
        cur, prev, check = self.find(self.head, None, value)
        if not check:
            raise ValueError
        elif  not prev:
            self.head = self.head.next
        elif cur == self.tail:
            prev.next = None
            self.tail = prev
        else:
            prev.next = cur.next

    def len(self):
        l = 0
        tmp = self.head
        while tmp:
            l+=1
            tmp = tmp.next
        return l
    
    def print(self):
        tmp = self.head
        while(tmp):
            print(tmp.value, end = "   ")
            tmp = tmp.next
        print()
