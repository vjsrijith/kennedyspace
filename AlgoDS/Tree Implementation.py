##################################################################################################################
#Tree implementation using Lists

# def BinaryTree(r):
#     return [r,[],[]]

# def getRootVal(r):
#     return r[0]

# def setRootVal(r,val):
#     r[0]=val
    
# def addLeft(r,val):
    
#     if len(r[1])>1:
#         temp=r[1]
#         r[1]=[[val],temp,[]]
#     else:
#         r[1]=[[val],[],[]]
    
#     return r
        
# def addRight(r,val):
#     if len(r[2])>1:
#         temp=r[2]
#         r[2]=[[val],[],temp]
#     else:
#         r[2]=[[val],[],[]]

#     return r
    
# def getLeft(r):
#     return r[1]

# def getRight(r):
#     return r[2]
        
# tree1=BinaryTree(10)  

# print(tree1)   
   
# tree1=addRight(tree1,30)
# tree1[2]=addRight(tree1[2],60)

# print(tree1)

# tree1=addLeft(tree1,20)
# tree1[1]=addLeft(tree1[1],40)

# print(tree1)


##################################################################################################################
#Tree implementation using class objects

class BinaryTree():
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None
    
    def addLeft(self,val):
         
        if self.left != None:
            temp=self.left
            self.left=BinaryTree(val)
            self.left.left=temp
        else:
            self.left=BinaryTree(val)
            
    def addRight(self,val):
         
        if self.right != None:
            temp=self.right
            self.right=BinaryTree(val)
            self.right.right=temp
        else:
            self.right=BinaryTree(val)
                
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
def BSTinsert(root,val):
    if root == None:
        return BinaryTree(val)
    else:
        if root.value==val:
            return root
        elif(root.value<val):
            root.right=BSTinsert(root.right,val)
        else:
            root.left=BSTinsert(root.left,val)        
    return root


def preorder (tree):
    if (tree!=None):
        print(tree.value)
        preorder(tree.getLeft())
        preorder(tree.getRight())

def inorder (tree):
    if (tree!=None):
        
        inorder(tree.getLeft())
        print(tree.value)
        inorder(tree.getRight())

def postorder (tree):
    if (tree!=None):
        
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.value)
        
        
# Tree1=BinaryTree(10)

# Tree1.addLeft(20)
# Tree1.addLeft(25)
# Tree1.addRight(30)
# Tree1.getLeft().getLeft().addLeft(35)
# Tree1.getLeft().getLeft().addRight(45)
# print(Tree1.value)
# print(Tree1.getLeft().value)
# print(Tree1.getRight().value)
# print(Tree1.getLeft().getLeft().value)
# print(Tree1.getLeft().getLeft().getLeft().value)
# print(Tree1.getLeft().getLeft().getRight().value)
   
# print('#####################')  
# print('Preorder')       
# preorder(Tree1)
# print('Inorder')
# inorder(Tree1)
# print('Postorder')
# postorder(Tree1)

#in_ls=[13, 3, 4]#, 12, 14, 10, 5, 1, 8, 2, 7, 9, 11, 6, 18]
r=BinaryTree(13)
r=BSTinsert(r,3)
r=BSTinsert(r,4)
r=BSTinsert(r,12)
r=BSTinsert(r,14)
r=BSTinsert(r,10)
r=BSTinsert(r,5)
r=BSTinsert(r,1)
r=BSTinsert(r,8)
r=BSTinsert(r,2)
r=BSTinsert(r,7)
r=BSTinsert(r,9)
r=BSTinsert(r,11)
r=BSTinsert(r,6)
r=BSTinsert(r,18)
preorder(r)



        