##lists 

#it is a datatype in python 
#strings  numbers boolean 

#primitive datatypes 
#they can store only single  value 
#they are immutable 


#list 
# it is a non primitive datatype
#it can store multiple values 
#it is mutable

#name age email mob  languages 

# print(type([1,2,3,4]))  #elements  seperated by comma  

# [1,2,3,4]-- homogenous list 
# ["hi","hello","how r u"]--homogenous datatype

# details=["mani",25,"not enough","hyd",500074,True,[]] #heterogenous

##sequence datatypes 
# strings   list tuple 

#list is  a ordered collection of elements

# print(details[0])
# print(details[len(details)-1]) 


# num[0]=0
# num[len(num)-1]=25
# print(num)
# for i in range(len(num)):
#     print(num[i])
# num[10]=11
# print(num)


# num=list((1,2,3,4,5,6))
# print(num)
# num=[1,2,3,4,5,6,7,8,9,10]  
# num.append(11) 
# num.append(12) 
# num.append((13,14,15)) 
# print(num)

# init + add
# l1=[1,2,3]
# l2=["happy","python","learning"]
# l1.extend(l2) 
# print(l1)
# num=[1,2,4,5]
# num.insert(10,3)
# print(num) 

# num=[1,2,3,4, 8,10]  #123498 10
# idx=4 
# ele=9  

# first=num[:idx]    ##[start:stop:step]  [0:4]  [1,2,3,4]
# second=num[idx:]  ##[4:]                       [8,10]
# first.append(ele) ##1234 +9  [1,2,3,4,9]
# first.extend(second) ##[1,2,3,4,9,8,10]
# print(first)

# lang.remove("css")
# print(lang)


lang=["js","java","css","python","css"]
#pop  

#without params -- removes last item 
#with param   -- removes  the item in the index
# lang.pop()
# print(lang)

#append extend insert  
#remove pop clear  
#sort index count reverse copy

# lang.clear()
# print(lang)


# animals.reverse()
# print(animals)

# num=[1,3,4,8,9,7,2,6,5]
# num.sort(reverse=True)
# print(num)

# animals=["cat","dog","lion","tiger","gorilla","frog","camel","cat"] 
# # animals.sort()
# # print(animals) 
# times=animals.count("c")
# print(times)


#index 
# animals=["cat","dog","lion","tiger","gorilla","frog","camel","cat"] 
# print(animals.index("cat"))


#copy 
# copied=color.copy() 

# copied.append("aqua")
# print(copied)
# print(color)

# color=["green","red","yellow","blue","black","white"] 


#count



# val="apple"
# count=0 

# for i in fruits:
#     if i==val:
#         count+=1
# print(f" {val} is present {count} times")

# for i in range(len(fruits)):
#     if fruits[i]==val:
#         print(i)
    

# fruits=["banana","apple","strawberry","orange","dragon","guava","papaya","guava","apple"]
# out=[]
# idx=2

# for i in range(len(fruits)):
#     if i==idx:
#         continue 
#     out.append(fruits[i])
# print(out)