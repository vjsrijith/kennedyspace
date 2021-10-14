##################################################################################################################
# Duplicate Column Rename
# col_list=['col1','col2','col3','col1','col1','col3']

# rn_col_list=[]

# for i,v in enumerate(col_list):
#     total_cnt=col_list.count(v)
#     cnt=col_list[:i].count(v)
#     rn_col_list.append((v+'_'+str(cnt)) if total_cnt>1 and cnt!=0 else v)
##df = df.toDF(*rn_col_list)
# print(rn_col_list)

##################################################################################################################
# Factorial
# n=4

# def factorial(num):
#     print(num)
#     return (1 if num==0 or num==1 else num*factorial(num-1))

# print(factorial(n))

##################################################################################################################
# Palindrome


# s='malayalam'
# #s1=s[::-1]


# l=len(s)-1
# print(l)
# for i,v in enumerate(s):
#     print(str(i)+' '+v)
#     print(str(l-i)+' '+s[(l-i)])
    
#print('Palindrome' if s1==s else 'Not a Palindrome' )

#################################################################################################################

#Fibbonaci

# n=10
# ls=[0]

# def fib(num):
#     return num

# for i in range(1,n):   
#     ls.append(1 if i==1 else ls[i-1]+ls[i-2])
    
# print(ls)


#################################################################################################################

#Fibbonaci
# def Fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#     # First Fibonacci number is 0
#     elif n==1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)

#################################################################################################################

#Armstrong Number

#num=153
# num=1634


# s=str(num)

# l=len(s)
# sum=0
# for i,v in enumerate(s):
#     sum+=int(v)**l

# print('Armstrong' if sum==num else 'Not an Armstrong')
    
###############################################################################################################
#Anagram Check - without considering the num of occurences

# s1='doaasg'
# s2='godsa'

# def Anagram_check(s1,s2):
    
#     for i in range(len(s1)):
#         if s2.count(s1[i])>0:
#             Anagram=True
#         else:
#             return False
#     return Anagram

# print(Anagram_check(s1, s2))
# print(Anagram_check(s2, s1))

# if Anagram_check(s1, s2) & Anagram_check(s2, s1):
#     print ("Anagram")
# else:
#     print ( "Not an Anagram")

###############################################################################################################
#Anagram Check - Considering the num of occurences
    
# s1='dogwww'
# s2='gowgwgd'
# str1=s1.replace(' ','').lower()
# str2=s2.replace(' ','').lower()
# #Solution 1
# print(True if sorted(str1)==sorted(str2) else False)

# count={}
# count1={}

# # if(len(str1)!=len(str2)):
# #     return False

# for i in str1:

#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1

# for j in str2:
#     if j in count1:
#         count1[j]+=1
#     else:
#         count1[j]=1
        
# print(count, count1)

# if(count==count1):
#     print('Anagram')
# else:
#     print('No Anagram')
###############################################################################################################
#Array-Pair Sum problem --Create possible pair arrays whose sum equal to k

# def pair_sum(ls,k):
#     out_list=set()
#     for i in range(len(ls)):
#         for j in range(i,len(ls)):
#             if ls[i]+ls[j]==k:
#                 out_list.add((ls[i],ls[j]))
#     return out_list

# print((pair_sum([1,3,2,2],4)))
            
###############################################################################################################
#Largest Continuous sum in a +/- elements array

# def cont_sum(ls):
#     max_sum=current_sum=ls[0]
#     for num in ls[1:]:
#         current_sum=max(current_sum+num,num)        
#         max_sum=max(current_sum,max_sum)
    
#     return max_sum        
    
# print(cont_sum([1,2,-1,3,4,10,10,-10,-1]))

###############################################################################################################
#Sentence Reversal

#str='This is'

# str_ls=str.split(' ')

# str_ls.reverse()
# out=''

# for i in range(0,len(str_ls)):
#     out+=str_ls[i]+' '
# print(out)
##############################################################################################################
#Sentence Reversal
# ls=[]
# i=0

# while i<len(str)-1:

#     word=''
#     while(str[i]!=' ' ):
#         word+=(str[i])
#         i+=1
#         if i==len(str):
#             break
#     ls.append(word)   
#     i+=1
# i=len(ls)-1
# word=''
# while i>=0 :
#     print(ls[i])
#     word+=ls[i]
#     word+=' '
#     i-=1

##############################################################################################################
#String Compression
# s='aaAAAbBBBB'
# str1=sorted(s)

# temp=''
# count=0
# print((count))
# ls=''
# for val in str1:
    
#     if val==temp:
#         count+=1
#     else:
#         ls+=(val+str(count))
#         count=0
#     temp=val

# print(ls)
##############################################################################################################
#Unique Character String

# s='abcde'

# s1=sorted(s)

# def check(s1):
#     temp=''
#     for val in s1:
#         if(val==temp):
#             return False       
#         else:
#             temp=val
        
#     return True

# print(check(s1))

##############################################################################################################
#Find the best profit from the below stock price



# def profit_func(arr):
#     profit=0
#     max_index=0
#     min_index=0
    
#     for i in range(1,len(arr)):
        
#         for j in range(0,i-1):
#             if arr[i]-arr[j]>profit:
#                 profit=arr[i]-arr[j]
#                 max_index=i
#                 min_index=j
    
#     print(arr[min_index],arr[max_index])    


# def profit_func(arr):
#     min_price=arr[0]
#     profit=0
    
#     for price in arr:
        
#         min_price=min(min_price,price)
#         profit_comparison=price-min_price
#         profit=max(profit,profit_comparison)
        
#     print(profit)
        
        
# stock=[5,11,13,6,30,10,4]

# profit_func(stock)    

##############################################################################################################
#Return the list with product of rest of elements

# def product_list(arr):
    
    
#     new_ls=[]
#     for ele in arr:
#         prod=1
#         for multiplier in arr:
#             if ele!=multiplier:
#                 prod*=multiplier
        
    
#         new_ls.append(prod)
        
#     return new_ls  
 
# ls=[1,2,3,4,5]
#print(product_list(ls))

##############################################################################################################
#Rectangle overlap problem

r1={'x':2,'y':4,'w':5,'h':12}
#r2={'x':4,'y':14,'w':3,'h':3}

r2={'x':1,'y':5,'w':7,'h':14}

r1_left=[r1.get('x'),r1.get('y')]
r1_right=[r1.get('x')+r1.get('w'),r1.get('y')+r1.get('h')]

r2_left=[r2.get('x'),r2.get('y')]
r2_right=[r2.get('x')+r2.get('w'),r2.get('y')+r2.get('h')]

print(r1_left)
print(r1_right)
print(r2_left)
print(r2_right)

interect_left=[max(r1_left[0],r2_left[0]),max(r1_left[1],r2_left[1])]
interect_right=[min(r1_right[0],r2_right[0]),min(r1_right[1],r2_right[1])]

print('Intersect')
print(interect_left)
print(interect_right)
