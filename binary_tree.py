class Tree:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

        

    def traverse(self):
        print(self.val)
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()
        
    
    def app (self,val):
        if self.val:
            if val<self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.app(val)
            elif val>self.val:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.app(val)
        else:
            self.val = val
           

        
                
          
tree = Tree(None)
test = [1,2,3]
for i in test:
    if i is None:
        continue
    tree.app(i)
tree.traverse()        
