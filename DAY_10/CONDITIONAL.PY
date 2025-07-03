
# WHAT 
# WHY 
# HOW + WHERE    


# APPLICATIONS
# WEB APPLICATIONS  --INST DASHBOARD  -EMAIL PASSWORD  --   LOGIN 
# MOBILE APPS 
# DESKTOP APPS 


# IF -- CONDITION 
# ELIF -- SHORT HAND NOTATION OF ELSE 
#ELSE 


# if  condition:
#     code block


# ticket=True
# if ticket==True:
#     print("saaho")


# signal="orange"
# if signal=="green":
#     print("you can go")
# else:
#     print("wait till signal is green")


# username="Manivardhan"
# if username=="manivardhan":
#     print("welcome user")
# else:
#     print("invalid credentials")



##login 
## username and password 

# username="username"
# password="secret"


# if username=="username" and password=="secret":
#     print("welcome")
# else:
#     print("invalid username or password")



# dress_color="red"   ## black or green
# if dress_color=="blue":
#     print("purchase 1")
# elif dress_color=="black":
#     print("purchase 2")
# elif dress_color=="green":
#     print("purchase 3")
# else:
#     print("good bye")
    

# signal="green"
# if signal=="green":
#     print("go")
# elif signal=="red":
#     print("stop")
# else:
#     print("wait")

##0- 12    -- child 
#13 -19   -- teenage 
#19 - 35  -- young 
# 35 - 55   -- adult 
# 55 - old


# age=70
# if age>0 and age<=12:
#     print("child")
# elif age>12 and age<=19:
#     print("teenager")
# elif age>19 and age<=35:
#     print("young") 
# elif age>35 and age<=55:
#     print("adult")
# else:
#     print("take rest")



# num=27   # 3
# if num%3==0:
#     print("multiple of 3")
# else:
#     print("not a multiple of 3")



# age = input("enter the age: ")##input will always be a string datatype
# print(type(age))



age=12 
citizen ="chineese"
 ##>18  and indian 
if age>18 and citizen=="indian":
    print("you are eligible")
elif citizen=="indian" and age<18:
    print("wait for some time")
else:
    print("go back to ur country")
    
    
    
    
###fundementals 
#operators datatypes condiational loops functions


##85 -a
#65-85 -b 
#50-65 -c 
#35-50 -d 
#else fail

age=20
if age>0 and age<=12:  
    print("child")

elif age>12 and age<=19:
    print("teenager")

elif age>19 and age<=35:
    print("young") 


elif age>35 and age<=55:
    print("adult")
    
else:
    print("take rest") 
##each if condition is checked