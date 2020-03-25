class node:
    head=None;
    data=None
    next=None
    def __init__(self,data=None):
        self.data=data
        self.next=None;
    
    def insertData(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            temp=self.head
            
            while temp is not None:
                temp=temp.next;
            temp=node(data)
            
    
    
    def printData(self):
        tmp=self.head
        while tmp is not None:
            print(tmp.data)
            tmp=tmp.next
        
        

llist=node()
llist.insertData(2)
llist.insertData(3)
llist.insertData(4)
llist.printData()       