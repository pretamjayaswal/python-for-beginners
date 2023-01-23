
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    # append Method
    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    # print Llist
    def print(self):
        current = self.head
        while current:
            print(current.value , end=' -> ')
            current = current.next
    # delete link
    def delete(self, value):
        ''' delete the first node with given value'''
        current = self.head
        if current.value == value:
            self.head = current.next 
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next 
            if current == None:
                return 
            
            prev.next = current.next 
            current = None 
    
    def insert(self, new_element, position):
        count = 1
        current = self.head

        if position == 1:
            new_element.next = current
            self.head = new_element
        
        while current:
            if count+1 == position:
                new_element.next = current.next
                current.next = new_element
                return 
            else:
                count += 1
                current = current.next 
            
# Testing methods   

e1 = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(40)
e5 = Node(50)

ex = Node(100)
ey = Node(200)

l1 = LinkedList()

l1.append(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)
l1.append(e5)

l1.print()
print("----------------------")

l1.insert(ex, 1)
l1.delete(20)

l1.print()


