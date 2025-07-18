##problem solving 

##lcm 
#least common multiple 
# n1=6  ##6 12 18 24 30 36 42 48 54 60
# n2=15 ##15 30 45 60 75 90 105 120 135 150 

# 29 58 ......290        20   580     30 870   31--899
# 31          310        20   620     30 930 


# n1=67  #   134 201                                          59 
# n2=59  #                                             67  
# big=0 
# small=0 
# if n1>n2:
#     big=n1 
#     small=n2
# else:
#     big=n2
#     small=n1  
# # big,small= (n1,n2) if n1>n2 else (n2,n1)
# if big%small==0:
#     print(big, " is the lcm")
# else:
#     lcm_not_found=True
#     temp_lcm= big+big   #134
#     while   lcm_not_found==True: 
#         if temp_lcm%n1==0 and temp_lcm%n2==0:  ##268%67 ==0 and 268%59==0
#             print(temp_lcm, " is the lcm")
#             break
#         else:
#             temp_lcm+=big ##134+67 201 268........
    
    
##GCD    // HCF  -- highest common factor
#greatest common divisor 

# n1=20  #1 2 4 5 10 20
# n2=22  #1 2 11 22 

# n1= 23  # 1 23
# n2=11   # 1 11
# small=0
# if n1<n2:
#     small=n1
# else:
#     small=n2 
# gcd=0
# for i in range(1,small+1):  ##
#     if n1%i==0 and n2%i==0: ##
#         gcd=i  #1 2 5  10
# print(gcd)


# b,p 
# return b**p
 
# write a function to convert min to hrs


# 360/60==6 
# min=180
# hrs=min//60  #2 
# rem=min%60  #10
# print("time is" , hrs, "hrs", rem, "mins")



# num=28
# s=0
# for i in range(1,num): #1 2 4 7 14     
#     if num%i==0:
#         s+=i 
# if s==num:
#     print("perfect number")
# else:
#     print("not perfect")

