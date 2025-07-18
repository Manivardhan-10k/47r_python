# string1="acegik"
# string2="bdfhjl" 
# #abcdefghijkl
# #for  no of iterations
# #while
# res=""
# for i  in range(len(string1)): ##0 1 2 3 4 5 
#     res+= string1[i]+string2[i]    ## 0-ab   1-cd   2-ef   3-gh   4-ij  5-kl
# print(res) 

# s1="13579"
# s2="2468"
# #1234564789 
# itr=0 
# res=""
# if len(s1)>len(s2): #5>4
#     itr=len(s1)
# else:
#     itr=len(s2)
# for i in range(itr):  ##0 1 2 3 4 
#      if i<len(s1) and i<len(s2):  ##0<5  0<4  1 1 2 2 3 3 4<5 4<4  
#         res+=s1[i]+s2[i] ##12 34 56 78
#      else:
#          res+=s1[i] #9
# print(res)


#truthsy values 

# non-empty string   including space
# if "1": ##truthsy value
#     print("true")
# else:
#     print("false")  

#non zero numbers  both +ve and -ve
# if 0:
#     print("valid value")  
# else:
#     print("invalid value")

#True
# if True:   #(5>3)
#     print("truthsy")
# else:
#     print("falsy")


# if None:
#     print("false")
# else:
#     print("true")

##non empty list
# print(len([""]))
# if [0]:
#     print("truthsy")
# else:
#     print("falsy")

##non empty dictionary
# if {"msg":"happy bday dhoni"}:
#     print(1)
# else:
#     print(0)


## non empty tuple 
# 
# if (0.1):
#     print(True)
# else:
#     print(False)
#falsy values 
#empty string
#zero(number)
#False
#None
#empty list
#empty dictionary
#empty tuple



# if not 0:
#     print("true")
# else:
#     print("false")


# sentence="there are different programming languages" ##
# words=sentence.split(" ")
# longest_word=""
# for i in range(len(words)):
#     if len(longest_word)<=len(words[i]) :
#         longest_word=words[i] 
# print(longest_word, " is the longest word")
# print(sentence.replace(longest_word,"something"))

# * * * * *
# *
# * * * * * 

#         *
# * * * * * 

rows=5 
mid=(rows//2)+1  ##2+1 3
for i in range(1,rows+1): #1 2 3 4 5
    res="" ##for storing the stars
    for j in range(1,rows+1):
        ##top half of the pattern
        if i<=mid:  ## <=3   
          if i==1 or i==mid or j==1:
              res+="*"+" "
          else:
              res+=" "+" " 
        #bottom half of the pattern
        else:
            if i==rows or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)
            

# * * * * *
#         *
# * * * * *
# *
# * * * * *  

# * * * * * 
#         *
# * * * * *
#         *
# * * * * * 