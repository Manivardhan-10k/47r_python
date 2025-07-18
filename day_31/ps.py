# #prime number 
# #divisible with 1 and itself 

# #2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 91 97 101 
# #1 2 4  --3 

# ##time complexity -- the time taken to execute the code
# # num=100 #1 2 4 5 10 20 25 50 100       30  -  1 2 3 5 6 10 15   30
# # factors=0
# # for i in range(2,(num//2)+1): #2 - 99
# #     if num%i==0:
# #         factors+=1  #
# #         break
# # if factors==0:
# #     print(num," is a prime number")
# # else:
# #     print("not prime  because it has ",factors,"factors")
    



# num=15 #31   47 -53    6-7    13-17 
# prime_not_found=True
# next_prime=0
# while prime_not_found==True:
#     num+=1  ##31 
#     factors=0 
#     for i in range(2,num): #2-30
#         if num%i==0:
#             factors+=1
#             break
#     if factors==0:
#         print("next prime number is",num)
#         next_prime=num
#         prime_not_found=False
    
    
# #prev prime 
# num=15  # 13        23
# prev_prime=0
# for i in range(num-1,1,-1): #15 --2   
#     #i-15
#     factors=0   
#     for j in range(2,i): #2-14 
#         if  i%j==0:
#             factors+=1
#             break
#     if factors==0:
#         print("prev prime is",i) 
#         prev_prime=i
#         break
    
         
# print(next_prime,prev_prime,num)
# #nearest prime 
# #             23   25      29
# #             29    30      3
# #             13    16      17
# if (num-prev_prime) <  (next_prime-num)   : ##2<4
#      print(prev_prime,"is the nearest prime")
# elif (next_prime-num)<(num-prev_prime):
#     print(next_prime,"is the nearest")
# else:
#     print("both are at equal distance")


#anagrams
# 2 strings 
#   silent listen 
#s-1,1    i-1,1   l-1,1   e-1,1  n-1,1 t-1,1 
#heart earth   ,   loop polo    , mama amma  , kaka akka, top pot  , tea eat 

# listens  silent

# s1="levi"
# s2="evil"
# if len(s1)!=len(s2):
#     print(s1,s2 , "are not anagrams")
# else:
#     is_anagram=True
#     for i in s1: #"l"  "e"
#         print(s1.count(i),s2.count(i))
#         if s1.count(i) !=s2.count(i):
#             is_anagram=False
#             break
#     if is_anagram==True:
#         print(s1,s2 ," are anagrams")
#     else:
#         print(s1,s2 , "are not anagrams")
            
            
        
    