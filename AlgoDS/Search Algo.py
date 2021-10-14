##################################################################################################################
#Sequential Search

# def seq_search_unordered(arr,item):
#     for ele in arr:
#         if ele==item:
#             return True
#     return False

# def seq_search_ordered(arr,item):
#     for ele in arr:
#         if ele==item:
#             return True
#         elif ele>item:
#             return False
#     return False

# ls=[2,3,1,7,5,6,4]
# print(seq_search_unordered(ls,2))

# ls=[1,3,5,7]
# print(seq_search_ordered(ls,4))

##################################################################################################################
#Binary Search

# def bin_search(arr,item):
#     print(arr)
#     if len(arr)==1 and arr[0]!=item:
#         return False
#     else:
#         if arr[len(arr)//2]==item:
#             return True

#         elif item>arr[len(arr)//2]:
#             return bin_search(arr[len(arr)//2:],item)
#         else:
#             return bin_search(arr[:len(arr)//2],item)

# ls=[1,3,5,7,9,11,13,15]
# print(bin_search(ls,4))


