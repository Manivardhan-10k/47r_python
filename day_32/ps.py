#num=10 
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
# pos=15
# count=0
# prime=0
# num=2 
# while count<pos: #0<7   1<7 
#     factors=0 
#     for i in range(2,num):
#         if num%i==0:
#             factors+=1
#             break 
#     if factors==0:
#         count+=1 
#         prime=num
#     num+=1
# #string formatting 
# print(f"{pos} prime number is {prime}")

# print(f"sum of 1+2 is {1+2}") 
# a=20 
# b=10 

# print(f"the difference between {a} and {b} is {a-b}")



# word="radhakrishna"
# sub="krish"
# for i in range(len(word)):#0 
#     if sub==word[i:i+len(sub)]: #0-4 1-4  2-4 3-4 4-4  
#        print(f" {sub} is a substring of {word} and is present at {i}-{i+len(sub) -1}")
#        break

#longest palindromic substring 
#ala
#aya
#layal
# word="malayali" #layal 
# longest="" #ala layal aya 
# i=0
# while i<len(word) and len(longest)<len(word[i::]): #0<8   0<8
#     temp=""
#     for j in range(i,len(word)): #0 1 2  3...
#         temp+=word[j]  
#         if temp==temp[::-1] and len(temp)>len(longest):
#             longest=temp   
#     i+=1
# print(longest)  


# scene  
# ethical hacking - department
# word="malayalam" # malayalam ala aya layal ala alayalam 







    







        
            
    