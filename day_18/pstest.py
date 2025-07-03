##even odd or zero 

# num=0 
# if num==0:
#     print("zero")
# elif num%2==0:
#     print("even")
# else:
#     print("odd")
    
##+ve -ve zero 

# num=-2 
# if num>0:
#     print("+ve")
# elif num<0:
#     print("-ve")
# else:
#     print("0")



#biggest of two 
num1=10
num2=20 

# if num1>num2:
#     print(num1,"is greater")
# else:
#     print(num2," is greater")
##ternary operator 
##true block if   else  
# print(num1, "is greater") if num1>num2 else print(num2, "is greater") 


# num=24
# print("multiple of 3 or 5") if num%3==0 or num%5==0 else print("not a multiple of 3 or 5")


#10 9 8 7 6 5 4 3 2 1  0

# for i in range(10,0,-1):      ###start stop-1 step
#     print(i)


# for z in range(1,20+1):
#     if z%2==0:
#         print(z)
# for z in range(2,20+1,2):
#         print(z)

# n=50
# total=0
# for i in range(1,n+1):
#     total+=i  #1 1+2  3+3 6+4 10+5
# print(total)
##1 X 1 = 1   .... 1 X 10 = 10 

# num=19 
# for i in range(1,11):
#     print(num, " X ",i," = ", num*i)



##5!  = 5 * 4 * 3 * 2 * 1   120
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i   ## fact = fact*i   fact=1*1  fact=1*2 
# print(fact)
 

# recursion


# def odd_nums():
#     for i in range(1,21):
#         if i%2!=0:
#             print(i)
# odd_nums()  
# odd_nums()  
# odd_nums()  

##palindrome 
##amma dad anna sis madam mom malayalam wow racecar  
# word="radar"
# # rev=word[::-1]
# ##last index will always be length -1
# rev=""
# last=len(word)-1  #3
# for i in range(last,-1,-1):
#     rev+=word[i] ## 3
# print(True) if word==rev else print(False)

#2 4 6 8 10

# def sum_in_10():
#     total=0
#     for i in range(1,11):
#         if i%2==0:
#             total+=i
#     return total 
# print(sum_in_10())
            
# def rev_num(num): #1234     123.4  4 43  432    4321  
#     rev=0 
#     while num!=0: #1234 123 12 1 0
#        last_digit=num%10  #4 3  2 1
#        rev= rev*10+last_digit ##0*10+4 4 4*10+3 43 43*10+2 432 432*10+1 4320+1 4321
#        num = num//10 ##1234//10 123.4 123 123//10 12.3 12  1.2  1 0.1 0
#     return rev
# print(rev_num(1234))

# mob=2848232124
# count=0
# while mob!=0:
#     last_digit=mob%10#
#     mob=mob//10 
#     count+=1 
#     if count==10:
#         if last_digit==9 or last_digit==8 or last_digit==7 or last_digit==6:
#           print("valid")
#         else:
#             print("invalid")
# print("valid") if count==10 else print("invalid")

# 9 8
# 7 6 