class Node():
    def __init__(self,val):
        self.value=val
        self.nextnode=None

class LinkedList():
    def __init__(self):
        self.head=None
    
    def traverse(self):

        temp=self.head
        while(temp):          
            print(temp.value)
            temp=temp.nextnode

    
    def addnode(self,value,pos):
        if pos==0:
            temp_head=self.head
            self.head=Node(value)
            self.head.nextnode=temp_head
        else:
            temp=self.head
            i=1
            while(i!=pos):
                temp=temp.nextnode
                i+=1
            new_next=temp.nextnode
            temp.nextnode=Node(value)
            temp.nextnode.nextnode=new_next
            
    def deletenode(self,val):
        prev=None
        Found=0
        if self.head.value == val:
            self.head=self.head.nextnode
            Found=1
        else:
            temp=self.head
            while temp and Found==0:
                
                if temp.value != val:
                    print('-----')
                    
                    
                    prev=temp
                    temp=temp.nextnode
                else:
                    # print('prevNext '+str(prev.nextnode.value))
                    # print('tempNext '+str(temp.nextnode.value))
                    prev.nextnode=temp.nextnode
                    Found=1
                
        return (False if Found==0 else True)
                    
                
                
    
list1=LinkedList()
list1.head=Node(10)

n2=Node(20)
list1.head.nextnode=n2
n3=Node(30)
n2.nextnode=n3
n4=Node(40)
n3.nextnode=n4
n5=Node(50)
n4.nextnode=n5
n6=Node(60)
n5.nextnode=n6

list1.addnode(35,2)
list1.addnode(5,0)
list1.addnode(65,7)

list1.traverse()
print('traverse')
print(list1.deletenode(10))
list1.traverse()