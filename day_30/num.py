# patterns 
#ps 
#thruthsy falsy 

#non empty string 
#non zero number 
#True 
#non empty list 
#          dictionary  {}
#          tuple


#"" 
# 0
#False 
#none 
#[]
#{}
#()



#upper lower find swapcase captialize split join replace title  isalpha isnum  isdigit
#count zfill strip lstrip rstrip rfind

# word="hello"  #2 3
# # print("hello".find("l"))
# last_index=0  #3
# char="l"
# for i in range(len(word)): #0 1 2 3 4 
#     if word[i]==char:
#         last_index=i  #2 3 
# print(last_index)



# number methods 

##
# print(abs(10))
# print(abs(-23))
# num= -123
# if num>0:
#     print(num)
# else:
#     print(num * -1)


# print(round(3.955,0)) #3.96 

##exponential values  
#base  power 
# print(pow(5,3))
# print(pow(5,-1))
# print(5**3)

## division modulus 
## quotient    reminder  


# divisor divident quotient reminder

# print(divmod(10,5))
# print(divmod(11,3))
# print(11//3,11%3)


# print(int(5.32))
# print(int("5"))

# print(float(5))
# print(round(float("5.132456789"),2)) 


# print(complex(2,3))
# print(2+3j)


# print(bin(1))
# print(bin(3)) 
# print(bin(8))  #1000
# print(bin(10))  #1000
# print(bin(16))  #  1 0 0 0 0 
# print(bin(32))  #  1 0 0 0 0 

# 236  
# print(bin(236)) 

# 6+10 16 
# 09af     0f 1e


# print(isinstance("hello",str))




# abs  round pow div mod int float complex bin oct hex isisntance type



##fibanocci series 
#0 1  1  2 3 5 8 13 21 34 55 89 144 233 377......
# a=0 
# b=1 
# for i in range(15):
#       print(a) #0  1  1 
#       c=a+b ##1   2
#       a=b  #1     1
#       b=c  #1      2
    
    
# a=0 
# b=1 
# limit=31
# for i in range(limit-1):
#         #34
#     c=a+b 
#     a=b  #55
#     b=c
# print(a)


#armstrong number 
# sum of digits raised to the power (no of digits) == num 
#153  
# 1**3 + 5**3 +3**3 =1+125+27 =153

# 1 5 3 
# num=153
# num2=num #153
# num3=num
# count=0
# while num!=0:  #153!=0   15!=0 1!=0 0!=0
#     ##153   153//10 15.3 15   15/10 1.5 1 1/10 0.1 0
#     num= num//10  #15 1 0
#     count+=1  #1 2 3  
# total=0
# while num2!=0: #153!=0  15!=0 1!=0 0!=0
#     last_digit= num2%10   # 3 5 1
#     total= total+ (last_digit**count) #0+3**3 27  27+(125) 152 152+1**3  152+1 153
#     num2=num2//10  ## 153//10   15.3 15  1.5 1 0.1 0    
# if total==num3:
#     print("armstrong")
# else:
#     print("not armstrong")

