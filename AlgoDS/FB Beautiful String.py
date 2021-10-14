# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 17:38:45 2021

@author: 212709023
"""

def eval(in_str):
    dict1={}
    list1=[]
    new_str=in_str.lower()
    
    for ele in new_str:
        
        dict1[ele]=new_str.count(ele)
    
    for k,v in dict1.items():
        list1.append(v)
    return sorted(list1,reverse=True)

inp='So I just go consult Professor Dalves'
inp1=''

for a in inp:
    if a.isalpha():
        inp1=inp1+a

ls=eval(inp1)

mul=26
sum1=0

for ele in ls:
    sum1+=ele*mul
    mul-=1

print(sum1)