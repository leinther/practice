class Node:
    def __init__(self,data):
        self.data = data #0
        self.next = None

        
    
class LinkedList:
    def __init__(self):
        self.head = None


        
    def append(self,data): #[2,3,4,5]
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
    

ll  = LinkedList()
ll.append(1)
ll.append(4)
ll.append(2)
ll.migrate(4,2)
ll.display()



