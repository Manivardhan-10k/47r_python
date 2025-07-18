# lists 

# mutating methods
# append 
# extend 
# insert --
# remove (value)
# pop(indx) 
# clear 
# reverse 
# sort -ascending (reverse=True) 

# non mutating 
# count 
# index
# copy



# num=[1,2,3,4,5,600] #21
# print(sum(num))


# highest=max(-5,2)
# print(highest)

# small=min(0,-2)
# print(small)


#to print the second highest value 
# num=[5,5,9,25,11,56,101,108,100]
# highest=max(num)#108
# num.remove(highest)
# sec_highest=max(num)
# print(sec_highest)


# num=[1,2]
# pos=3

# for i in range(pos):
#     highest=max(num)
#     num.remove(highest)
# print(max(num))

## to remove duplicates from the list
# num=[9,8,6,76,9,60,78,99,105,203,256,256,256,256] #8
# unq_num=[]
# for i in num: #9
#     if i not in unq_num:
#         unq_num.append(i) #9 8 6 76  
# print(unq_num)
# pos=40
# if len(unq_num)<pos:
#     print("not possible")
# else:
#  for i in range(pos-1):
#     # high=max(unq_num)
#     unq_num.remove(max(unq_num))
#  print(max(unq_num))
    
    
    
    




# def find_highest(li,n):  
#     if len(li)<n:
#         return "not possible"
#     else:
#         for i in range(n):
#             li.remove(max(li)) ##
#         return max(li)
# print(find_highest(num,pos))
    
    
    
    
    
# num=[-256,-256,-256,-104,-108,-100,-2000,-10000]
# temp=num[0] #-256
# for i in num:#256 
#     if i<temp:
#         temp=i #-104 -100
# print(temp)  
    
    
# num=[1,2,3,4,5,6]#21 
# temp=0
# for i in num:
#     temp+=i
# print(temp)  


# to return the index of value
# food=["biryani","pizza","fried_rice","manchuria","momo","fish","rasmalai","laddu","ice cream","momo"]
# val="momo"
# for i in range(len(food)):
#     if food[i]==val:
#         print(f" {val} is present at {i+1} position")
#         break

# food=["biryani","pizza","fried_rice","manchuria","momo","fish","rasmalai","laddu","ice cream","momo","momo"]
# count=0 
# item="momo"
# for i in food:
#     if i==item:
#         count+=1
# print(f"{item} is present {count} times")


# movies=["salar","kgf","akhanda2","og","dil"]
# rev=[]
# for i in range(len(movies)-1,-1,-1):
#     rev.append(movies[i])
# print(rev)

# chars=[1,"A","B",2,"a","z"]
##ord()   uc 65-90   
##97-122   lc
# uc="AB"
# lc="az"
# sum=3