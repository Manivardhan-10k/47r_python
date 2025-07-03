# nested loops
# doing the same thing again again 

#for 
#when the no of repetetions/iterations are finite

#while
#untill the condition is satisfied 


#print 1-5 tables upto 10 multiples 
# 1 X 1 = 1 .....  5 X 10 =50
# for i in range(1,6): ##1 2 3  4 5
#     for j in range(1,11):
#         if j==5:
#             continue  
#         print(i ,"X ", j, " =",i*j)
        

# control statements 
# break 
# continue
# pass       
# 1*1 =1

# for i in range(1,6):
#     for j in range(1,11):
#         if i*j>25:
#             break
#         print(i,"X ",j,"= ",i*j)
        

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
   
#no of rows= 5


# rows=int(input("enter the no of rows: "))
# #first loop will always be for rows 
# for i in range(1,rows+1): #1 2
#     ##starting of row
#    pattern=""    #for storing stars
# #nested loop is for columns 
#    for j in range(1,rows+1): #1 2 3  4 5
#        pattern +="* "     #* * * * * 
#    print(pattern)



# * 
# * *
# * * *
# * * * *
# * * * * * 

# rows=5 
# #for rows 
# for i in range(1,rows+1): #1 2 3 4 5
#     pattern="" 
#     for j in range(1,i+1): # 1-3 1-4 1-5 1-6
#         pattern+= "*"+" "  ##*   * *    * * *   * * * *   * * * * *
#     print(pattern)
    

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 
# rows=5 
# for i in range(1,rows+1):
#     pattern="" 
#     for j in range(1,i+1):
#         pattern += str(j) +" "
#     print(pattern)


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5

# rows=5

# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+= str(i)+" "
#     print(pattern)
    
    
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# rows=4 
# num=1
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+=  str(num)+" "
#         num+=1
#     print(pattern)



# 2 
# 4 6
# 8 10 12
# 14 16 18 20

# rows=4 
# num=2
# for i in range(rows):#0 1 2 3 
#     res=""  ##storing the values 
#     for j in range(i+1): #0 1 
#         res+= str(num)+ " "
#         num+=2
#     print(res)
    
        
    




# 1 
# 3 5
# 7 9 11
# 13 15 17 19

# rows=4 
# num=1 
# for i in range(rows):
#     res=""
#     for j in range(i+1):
#         res += str(num)+" "
#         num+=2 
#     print(res)
        