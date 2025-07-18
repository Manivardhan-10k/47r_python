# s="9999"
# res=""
# # double 9 triple 7 double 6 one 2 one 3 one1 
# i=0 
# while i<len(s):
#     count=1 
#     for j in range(i,len(s)-1): #0-10
#         if s[j+1]==s[j]:
#             count+=1       
#         else:
#             if count==1:
#                 res+="one"+s[i]+" "
#             elif count==2:
#                 res+="double"+s[i]+" "
#             elif count==3:
#                 res+="triple"+s[i]+" "
#             elif count==4:
#                 res+="quad"+s[i]+" " 
#             break
#     i+=count
#     if i==len(s)-1:
#         res+= "one"+s[i]+" "
#         break
# print(res)
        
        
    
    
#nested list 
# nested=[1,[2,3]] 
# sum=0
# for i in nested: #1  [2,3]
#    if isinstance(i,list):
#        for j in i:
#            sum+=j  ##1+2  3+3 6
#    else:
#        sum+=i #0+1
# print(sum) 


# print(isinstance(1,int))
# print(isinstance("python",str))
# print(isinstance(True,bool))
# print(isinstance(2.3,float))
# print(isinstance({},dict))
# print(isinstance(2+3j,complex))
# print(isinstance([],list))
# print(isinstance((),tuple)) 


# nested=[[1,20],[3,4],[4,50]]
# max_list=nested[0]
# max_val=nested[0][0] 

# for i in nested: ##[1,2]
#     temp=0
#     for j in i:#1,2
#         temp+=j  #3 
#     if temp>max_val:
#         max_val=temp 
#         max_list=i
# print(max_val,max_list)






# nested=[[1,20],[3,4],[4,50]]
# maximum=nested[0][0]  #1 
# for i in nested:
#     for j in i:
#         if j>maximum:
#             maximum=j 
# print(maximum) 


# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rows=len(matrix) #3 
# # cols=len(matrix[0]) #3
# square=True
# for i in matrix:# [1 2 3] 
#     if rows==len(i): #3==3
#       pass 
#     else:
#         square=False
#         break      
# if square:
#     print(f"{matrix} is  a square matrix") 
# else:   
#     print(f"{matrix} is not a square matrix")    
    





