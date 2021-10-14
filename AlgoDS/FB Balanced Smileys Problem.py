# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:27:16 2021

@author: 212709023
"""


#5

# :((
# i am sick today (:()
# (:)
# hacker cup: started :):)
# )(


def cleanup(in_str):
    new_str=[]
    for i in range(0,len(in_str)-1):
        if in_str[i] in ['(',')']:
            new_str.append(in_str[i])
        elif in_str[i]==':' and in_str[i+1] in ['(',')']:
            new_str.append(in_str[i])
            
    if in_str[len(in_str)-1] in ['(',')']:
        new_str.append(in_str[len(in_str)-1])
    return new_str

def check(new_str):
    stack=[]
    if len(new_str)==0:
        return True
    elif new_str[0] =='(':
        stack.append('(')
    elif new_str[0] ==')':
        return False

    
    for i in range(1,len(new_str)):
        if new_str[i] =='(' and new_str[i-1]!=':':
            stack.append('(')
        elif new_str[i] ==')' and new_str[i-1]!=':':
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
    
    

s=cleanup('asdg')
print(s)
print(check(s))
