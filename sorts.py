
                                                   ### SELECTON SORT ###

# a=list(map(int,input().split()))

# for i in range(len(a)):
#   large_index= i
#   for j in range(i+1,len(a)):
#     if(a[j] > a[large_index]):
#       large_index=j

#   if(large_index!=i):
#     # temp=a[i]
#     # a[i]=a[large_index]
#     # a[large_index]=temp
        
#     a[i],a[large_index]=a[large_index],a[i]#Easy Way to Swap#


# print(a)


                                                     ### Bubble sort ####

# a= a=list(map(int,input().split()))

# for i in range(len(a)):
#   for j in range(i+1,len(a)):
#     if(a[j-1] > a[j]):
#       a[j-1],a[j]=a[j],a[j-1]


# print(a)



                                                    ####  Insertion Sort   ####
# a= a=list(map(int,input().split()))

# for i in range(1,len(a)):
#     for j in range(i):
#         if(a[i]<a[j]):
#             temp=a[i]
#             for x in range(i,j,-1):
#                 a[x]=a[x-1]
#             a[j]=temp
        
# print(a)


                                                       ### Merge Sort ####



# def mergesort(start,end):
#     if(start<end):
#         mid=int((start+end)/2)
#         mergesort(start,mid)
#         mergesort(mid+1,end)
#         merge(start,mid,end)

# def merge(start,mid,end):
  

#     temp=[0]*len(a)
#     i = start
#     j = mid+1
#     k = start
    
#     while(i<=mid and j<=end):
#         if(a[i]<=a[j]):
#             temp[k]=a[i]
#             i+=1
#             k+=1
#         else:
#             temp[k]=a[j]
#             j+=1
#             k+=1

#     if(i>mid):
#         while(j<=end):
#             temp[k]=a[j]
#             j+=1
#             k+=1
#     if(j>end):
#         while(i<=mid):
#             temp[k]=a[i]
#             i+=1
#             k+=1
    

#     for i in range(start,end+1):
#         a[i]= temp[i]
    
   
# a=list(map(int,input().split()))
# mergesort(0,len(a)-1)
# print(a)

