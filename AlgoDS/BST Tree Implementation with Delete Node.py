class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
    
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def addLeft(self,item):
        if self.left==None:
            self.left=BinaryTree(item)
        else:
            temp=self.left
            self.left=BinaryTree(item)
            self.left.left=temp
    
    def addRight(self,item):
        if self.right==None:
            self.right=BinaryTree(item)
        else:
            temp=self.right
            self.right=BinaryTree(item)
            self.right.right=temp
            
def preOrder(tree):
    if tree!=None:
        print(tree.value)
        preOrder(tree.getLeft())
        preOrder(tree.getRight())
        
def inOrder(tree):
    if tree!=None:
        inOrder(tree.getLeft())
        print(tree.value)
        inOrder(tree.getRight())
        
def postOrder(tree):
    if tree!=None:
        postOrder(tree.getLeft())
        postOrder(tree.getRight())
        print(tree.value)
        
def BS_Tree_Insert(root,item):
    if root==None:
        return BinaryTree(item)
    elif root.value==item:
        return root
    elif root.value<item:
        root.right=BS_Tree_Insert(root.right,item)
    else:
        root.left=BS_Tree_Insert(root.left,item)
    return root

def minNode(root):
    while root.left!=None:
        root=root.left
    
    return root

def maxNode(root):
    while root.right!=None:
        root=root.right
    
    return root

def minValueNode(root):
    while root.left!=None:
        root=root.left
    
    return root

def deletenode(root,key):
    if root==None:
        
        return root
    elif  root.value>key:
        print('Go Left')
        root.left=deletenode(root.left, key)

    elif root.value<key:
        print('Go Right')
        root.right=deletenode(root.right,key)
        
    #when root.value==Key
    else:
        print('Key Found')
        if root.left==None:
            print('left Child==None check passed')
            temp=root.right
            root=None
            print(temp.value if temp is not None else None)
            return temp
        elif root.right==None:
            print('Right Child==None check passed')
            temp=root.left
            root=None
            print(temp.value if temp is not None else None)
            return temp
        else:
            print('Right and Left child found')
            #Have right and left
            temp=minNode(root.right)
            root.value=temp.value
            root.right=deletenode(root.right,temp.value)
            
    return root
            
   
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.value:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.value):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.value = temp.value
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.value)
 
    return root     

def searchNodeRec(root,key):
    if root==None:
        return root    
    elif root.value==key:
        return root
    elif root.value>key:
        return searchNodeRec(root.left,key)
    else:
        return searchNodeRec(root.right,key)
    
def searchNode(root,key):
    
    while root.value != key:
        if root.value>key:
            root=root.left
        else:
            root=root.right
    return root

def MinimumFromNode(root,key):
    Node=searchNode(root,key)
    return minNode(Node)

level_dict={}
def LevelWisePrint(root,level):
    
    if root!=None:

        #if root.value not in level_dict:
        level_dict[root.value]=level
        level=level+1
        if root.left!=None:
            level_dict[root.left.value]=level
            LevelWisePrint(root.left,level)
            
        if root.right!=None:
            level_dict[root.right.value]=level
            LevelWisePrint(root.right,level)

def Trim_BST(root,min_value,max_value):
    if root is None:
        return
    
    root.left=Trim_BST(root.left,min_value,max_value)
    root.right=Trim_BST(root.right,min_value,max_value)
    
    if min_value<=root.value<=max_value:
        return root
    if root.value<min_value:
        return root.right
    if root.value>max_value:
        return root.left
    
    


N=BinaryTree(10)
# N.addLeft(5)
# N.addRight(15)

BS_Tree_Insert(N, 5)
BS_Tree_Insert(N, 15)
BS_Tree_Insert(N, 12)
BS_Tree_Insert(N, 6)
BS_Tree_Insert(N, 3)
BS_Tree_Insert(N, 20)
BS_Tree_Insert(N, 2)
BS_Tree_Insert(N, 4)
BS_Tree_Insert(N, 7)
BS_Tree_Insert(N, 11)
BS_Tree_Insert(N, 13)
BS_Tree_Insert(N, 18)
BS_Tree_Insert(N, 22)
# print('Pre')
# Order(N)
# print('##In##')
# inOrder(N)
# # print('Post')
# # postOrder(N)
# #N=deletenode(N,15)
# print('##In##') 
# inOrder(N)

print('Max:'+str(maxNode(N).value))
print('Min:'+str(minNode(N).value))

print(searchNodeRec(N,22).value)
print(searchNode(N,10).value)


print('MinimumFromNode: '+str(MinimumFromNode(N,20).value))

LevelWisePrint(N,1)
print(level_dict)
max_level=max(list(level_dict.values()))

for i in range(1,max_level+1):
    print()
    for k,v in level_dict.items():
        if v==i:
            print(k,end=' ')


N1=Trim_BST(N, 6, 18)

print('\n##In##') 
inOrder(N1)