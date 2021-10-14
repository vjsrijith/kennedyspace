#####################################################################################
################################## QUEUE ############################################
#####################################################################################

class queue():
    
    def __init__(self):
        self.items=[]
    
    def isempty(self):
        return (True if len(self.items)==0 else False)
    
    def enqueue(self,item):
        
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def print_queue(self):
        return self.items
    

        

s1=queue()

print(s1.isempty())

s1.enqueue(1)
s1.enqueue('a')
s1.enqueue('b')
s1.enqueue('c')
print(s1.print_queue())
print(s1.dequeue())

print(s1.print_queue())
        
print(s1.dequeue())

print(s1.print_queue())


# #using only append and pop
# #Not allowed to use insert(0,val) and pop(0)

# class Queue2Stack():
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
    
#     def enqueue(self,item):
#         self.stack1.append(item)

    
#     def dequeue(self):
#         self.stack2=[]
#         for i in range(len(self.stack1)-1,0,-1):
#             self.stack2.append(self.stack1[i])
#         #popped_val= self.stack2.pop()
       
#         self.stack1=[]
#         self.stack1=self.stack2[::-1]
        
#         return True
    
#     def printQ(self):
#         print(self.stack1)
    
# que1=Queue2Stack()

# que1.enqueue(1)
# que1.enqueue(2)
# que1.enqueue(3)
# que1.printQ()

# que1.dequeue()
# que1.printQ()

# que1.enqueue(1)
# que1.printQ()

# que1.dequeue()
# que1.printQ()
