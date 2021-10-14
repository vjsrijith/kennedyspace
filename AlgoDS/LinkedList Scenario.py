class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self,node):
        self.head=node
        
    def traverse(self):
        print('Traverse')
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
        
    def List_length(self):
        i=0
        temp=self.head
        while temp:
            temp=temp.next
            i+=1
        return i
            
    def addNode(self,pos,value):

        temp=self.head
        i=1
        if pos==0:
                
            self.head=node(value)
            self.head.next=temp
        else:
            while temp and i!=pos:
                temp=temp.next
                i+=1
                
            nextnode=temp.next
            temp.next=node(value)
            temp.next.next=nextnode   
            
    def deleteNode(self,value):

        temp=self.head
        if temp.value==value:
            self.head=temp.next
            return True
            
        else:            
            while temp.next:
                #temp=temp.next
                if temp.next.value==value:
                    
                    cur=temp.next
                    temp.next=cur.next
                    return True
                else:
                    temp=temp.next
        return False                            
    
    def detectLoop(self):
        checklist = []
        temp = self.head
        while (temp):
            if (temp in checklist):
                return True
            checklist.append(temp)
 
            temp = temp.next
 
        return False
    
    def cycleAdd(self,value,pos):
        
        last=temp=self.head
        i=0
        while last.next:
            last=last.next
        new=node(value)
        last.next=new
        
        while temp and i!=pos :
            temp=temp.next
            i+=0
        #cycle back to head
        new.next=self.head
      
    def reverseList(self):
        list_collect=[]
        temp=self.head
        
        while temp:
            list_collect.append(temp.value)
            temp=temp.next
        list_collect.reverse()
        
        print(list_collect)
        rev_head=node(list_collect[0])
        rev_list=LinkedList(rev_head)
        
        for i in range(1,len(list_collect)):
            rev_list.addNode(i,list_collect[i])
        
        return rev_list
    
    def reverseList1(self):
        current=self.head
        prevnode=None
        nextnode=None
        
        while current:
            nextnode=current.next # to be used to traverse forward in the linkedlist
            current.next=prevnode
                
            prevnode=current
            current=nextnode
        return LinkedList(prevnode)
    
    
    def nth_to_LastNode(self,n):
        leftMark=self.head
        rightMark=self.head

        i=0
        while i!=n:
            rightMark=rightMark.next#1
            i+=1
            
        while rightMark:
            rightMark=rightMark.next 
            leftMark=leftMark.next
        
        return leftMark.value

        
H=node(10)
list1=LinkedList(H)
list1.addNode(1,20)
list1.addNode(2,30)
list1.addNode(1,15)
list1.addNode(3,25)
list1.addNode(3,30)
list1.addNode(6,35)
# list1.addNode(7,40)
# list1.addNode(7,38)

# (list1.deleteNode(25))
# (list1.deleteNode(40))
list1.traverse()

#list1.cycleAdd(100,4)

# print('***')
# print('loop Check: ',list1.detectLoop() )

# revList=list1.reverseList()
# revList.traverse()

# revList1=list1.reverseList1()
# revList1.traverse()
print('**************')

print(list1.nth_to_LastNode(5))
