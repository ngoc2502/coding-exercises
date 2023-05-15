# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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

def num_from_list(list):
    node = list.head
    len_num = list.len()

    num = 0
    while node:
        len_num = len_num -1
        num += 10**(len_num) * node.value
        node = node.next
    return num

def solve_proplem(list1, list2):
    num1 = num_from_list(list1)
    num2 = num_from_list(list2)
    
    num_plus = num1 + num2

    result = LinkedList()
    
    while num_plus:
        result.insert(num_plus % 10)
        num_plus = int(num_plus/10)

    return result


arr1 = [1,3,4,2]
arr2 = [1,3,2,1]
l1 = LinkedList()
l2 = LinkedList()
for i in arr1:
    l1.insert(i)
for i in arr2:
    l2.insert(i)

re = solve_proplem(l1,l2)
re.print()


            
        

            
    
        