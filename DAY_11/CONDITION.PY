# conditional statement  
# if  -- to check the condition

# elif -- alternate condition

# else -- what if condition fails


# if condition:
#     code block


# age=19

# if age>=18:
#     print("eligible to vote")
    

    
    
# else:
    
# num=1

# if num==1:
#     print("one")
# elif num==2:
#     print("two")
# elif num==3:
#     print("three")
# else:
#     print("num >10")

#simple if 
##ternary operator 

# true block  if condition  else  false block

# if condition:
#     block 
# else:
#     block 

# age=17
# print ("eligible") if age>=18 else print("not eligible")  

# 3.12
# match:case 


# match -- compares the values

# day=10
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursday")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:    ##default case   _  (similar to else block)
#         print("invalid day")


# cleaner code:
#condition   -- single condition    
#values -- there can be multiple values



# month=0
# match month:
#     case 0:
#         print("jan")
#     case 5:
#         print("jun")
#     case _:
#         print("invalid month") 


# num=15 
# if num%2==0:
#     print("even")
# else:
#     print("odd")
    
# Write a program to check if a number is positive, negative, or zero.

# num=0.5
# if num>0:
#     print("positive")
# elif num==0:
#     print("zero")
# else:
#     print("negitive")


# Write a program to check if a number is divisible by both 3 and 5. 
##15 30 45  60 75 90 105 120 135 150....
# num=90
# if num%5==0 and num%3!=0:
#     print("divisible by only 5")
# elif  num%3==0 and num%5==0:
#     print("divisible both 3 and 5")
# elif num%3==0 and num%5!=0  :
#     print("divisible by only 3")
# else:
#     print("not divisible")

# n1=10 
# n2=10 
# if n1>n2:
#     print(n1,"is greater")
# elif n2>n1:
#     print(n2, "is greater")
# else:
#     print("both are equal")





# teranary operator 
# true block if condition else false block



# match case:
# init value 
# match intvalue:
#     case val:
#         code block 
#     case val2:
#         code block 
#     case _:
#         code block
# month 1 - 12  - >12 