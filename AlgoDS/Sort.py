##################################################################################################################
#Bubble Sort
#Swap and push the max element to the last ele of the loop

# def bubble_sort(arr):
    
#     for n in range(len(arr)-1,0,-1):
#         for k in range(n):
#             if arr[k]>arr[k+1]:
#                 temp=arr[k]
#                 arr[k]=arr[k+1]
#                 arr[k+1]=temp
#     return arr

# ls=[5,4,6,8,2,7,1]

# print(bubble_sort(ls))

##################################################################################################################
#Selection Sort
#Select the ele position with max and replace with last ele of the loop

# def selection_sort(arr):
    
#     for n in range(len(arr)-1,0,-1):

#         pos_max=0
#         print('n=',n)
#         for k in range(n+1):
#             if arr[k]>arr[pos_max]:
#                 pos_max=k
#         temp=arr[n]
#         arr[n]=arr[pos_max]
#         arr[pos_max]=temp
#     return arr

# ls=[5,4,6,8,2,7,1]

# print(selection_sort(ls))

##################################################################################################################
#Insertion Sort
#Assuming first ele is part of the sorted sublist. 
#Go on adding the new ele to this sublist at the appropriate place


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         currentvalue=arr[i]
#         position=i
        
#         while position>0 and arr[position-1]>currentvalue:
#             arr[position]=arr[position-1]
#             position=position-1
        
#         arr[position]=currentvalue
    
# ls=[5,4,6,8,2,7,1]
# insertion_sort(ls)
# print(ls)

##################################################################################################################
#Merge Sort
def MergeSort(arr):

    if len(arr)>1:

        mid=len(arr)//2
        leftHalf=arr[:mid]
        rightHalf=arr[mid:]

        MergeSort(leftHalf)
        MergeSort(rightHalf)

        i=j=k=0

        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                arr[k]=leftHalf[i]
                i+=1
            else:
                arr[k]=rightHalf[j]
                j+=1
            k+=1

        while i<len(leftHalf):
            arr[k]=leftHalf[i]
            i+=1
            k+=1
        while j<len(rightHalf):
            arr[k]=rightHalf[j]
            j+=1
            k+=1
    print(arr)
