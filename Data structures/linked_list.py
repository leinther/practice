class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert (self,args):
        new_node = Node(args)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next 
        current.next = new_node
    
    def display(self):
        root = self.head
        while root:
            print(root.val)
            root = root.next         

    def revers(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def middle (self):
        slow,fast = self.head, self.head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow 
            
    def plndr (self):
        curr = self.middle()
        prev = None 
        while curr.next:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp
        l = self.head
        l,r = self.head, prev 
        while r:
            if l.val != r.val:
                return False
            print (l.val,r.val)
            l,r = l.next, r.next
        return True





head = LinkedList()
nums = [1,1,2,1,1]
for val in nums:
    head.insert(val)
print(head.plndr())

