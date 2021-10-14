#####################################################################################
################################## DEQUE ############################################
#####################################################################################

class deque():
    
    def __init__(self):
        self.items=[]
    
    def isempty(self):
        return (True if len(self.items)==0 else False)
    
    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def print_queue(self):
        return self.items
        

s1=deque()

print(s1.isempty())

s1.addFront('a')
s1.addFront('b')
s1.addRear('c')
s1.addRear('d')

print(s1.print_queue())

s1.removeFront()
s1.removeRear()

print(s1.print_queue())
        