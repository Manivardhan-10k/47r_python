# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1


# rows=5 
# for row in range(rows): ##0 1 2 3 4
#     res=""
#     for col in range(row+1):#01   02  03  04  05
#         res+= str(rows)+ " " ##""+5 
#     rows=rows-1 #4
#     print(res)



# 5 5 5 5 5
# 4 4 4 4 
# 3 3 3 
# 2 2
# 1 

# rows=5 
# for i in range(rows,0,-1): #5 4 3 2 1 
#     res=""
#     for j in range(1,i+1):
#         res+= str(i)+" "
#     print(res)


# * * * * *
# *       * 
# *       * 
# *       * 
# * * * * *

# rows =9
# for i in range(1,rows+1): #1 2 3 4 5
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows:
#            res+="*"+" "
#         else:
#             res+=" "+" "# one space is for char second space is for btwn char space
#     print(res)


# * * * * 
# * 
# * 
# *
# * * * *  
# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows):
#         if i==1 or i==rows or j==1:
#             res+="*"+" "          
#     print(res)   

# * * * * *
# *
# * * * * *
# *
# * * * * *
# rows=5 
# for i in range(1,rows+1): #1 2 3 4 5
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or i==(rows//2)+1:
#             res+="*"+" "
#     print(res)

# * * * * *
#     *
#     *
#     *
# * * * * *
# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j== (rows//2)+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)





rows=5 
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j  or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
    
    
    
# *       *
# *       *
# * * * * *
# *       *
# *       *

# * * * * *
#     *
#     *
#     *
#     *

# *       *
# * *     *
# *   *   *
# *     * *
# *       * 


# * * * * *
#       *
#     *   
#   *
# * * * * * 