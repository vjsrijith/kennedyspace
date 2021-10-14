#In case of recursion always identify the base case.

#Cumulative Sum

# def cumu_sum(n):
#     if n==0:
#         return 0
#     else :
#         return n+cumu_sum(n-1)
# print(cumu_sum(4))

##################################################################################################################

#SUM of digits

# def digit_sum(n):
#     s=str(n)
    
#     if len(s)==1:
#         return int(s)
#     else:
#         return int(s[0])+digit_sum(int(s[1:]))

# print(digit_sum(5432))

# def digit_sum(n):
    
#     if int(n/10)==0:
#         return n
#     else:
#         return n%10 + digit_sum(int(n/10))
    
# print(digit_sum(5432))

##################################################################################################################
#Phrase in word list

# def findwords(phrase,wordslist,ls_out=None):
    
#     if ls_out is None:
#         ls_out=[]
#     for word in wordslist:
        
#         if phrase.startswith(word):
#             ls_out.append(word)
#             return findwords(phrase[len(word):],wordslist,ls_out)
#     return ls_out  
# print(findwords('themanran',['the','man','rab']))

##################################################################################################################
#Reverse a string

# def reverse(s1):
    
#     if len(s1)==0:
#         return s1
#     else:
#         return reverse(s1[1:])+s1[0]

# print(reverse('hello world'))


##################################################################################################################
#String permutaton


