#####################################################################################
################################## STACK ############################################
#####################################################################################

# class stack():
    
#     def __init__(self):
#         self.items=[]
    
#     def isempty(self):
#         return (True if len(self.items)==0 else False)
    
#     def push(self,item):
#         self.items.append(item)
    
#     def pop(self):
#         return self.items.pop()
        
#     def peek(self):
#         return self.items[len(self.items)-1]
        

# s1=stack()

# print(s1.isempty())

# s1.push(1)
# s1.push('a')
# s1.push('b')
# s1.push('c')

# print(s1.pop())

# print(s1.peek())

#####################################################################################
#Balanced Parenthesis problem

open_paren=['(','[','{']
paren_set=[('(',')'),('[',']'),('{','}')]
stack=[]
last_open=''
def balanced(str_paren):
    if len(str_paren)%2!=0:
        return False
    
    for val in str_paren:
        if val in open_paren:
            stack.append(val)
        else:
            if len(stack)==0:
                return False
            else:
                last_open=stack.pop()
                if (last_open,val) not in paren_set:
                    return False
    return len(stack)==0

print(balanced('[[({}))]'))
              