## startswith
##endswith 
# .isalpha()
# isdigit  
# isalnum 
# swapcase 
# zfill
#split--seperator =[]
# word="koushik"
# word=list(word)
# word[0]="K"
# word="".join(word)
# print(word)

# ASCII : 
# American Standard Code for Information Interchange

#binary 0or1

# converted into binary 
# 1   -1 
# 2   10 
# 11

# a  -  97  


# 0-127 

# a-z   -- 97 -122 
# A -Z     65 -- 90
# 0-9      48-  57


# printable -32 


# aplhabets 


# 65-90 
# 97-122 
# 48-57

#ord --order

# print(ord("S"))  # 65-90
# print(ord("m"))  #97-122
# print(ord("9"))

# char="u" #65-90  97-122
# asc_code=ord(char)
# if asc_code>=97 and asc_code<=122:
#     print("lower case")
# else:
#     print("not lower case")







# char="2"   ##lowercase 
# code=ord(char) 
# if code>=65 and code<=90:
#     print("upper case")
# elif code>=97 and code<=122:
#     print("lower case")
# else:
#     print("not alphabet")


# code=89 
# #chr --character 
# print(chr(code))

# ord()
# chr()


# sentence="Ee Nagaraniki Emaindhi"
# upper_count=0
# for i in range(len(sentence)):
#     code= ord(sentence[i])  
#     if code>=65 and code<=90:
#         upper_count+=1
# print("there are ",upper_count,"uppercase characters")



# ord()
#chr()
# name="chitti"   ## dijuuj
# secret=""
# for i in range(len(name)):
#     code=ord(name[i])  #99 
#     new_char=chr(code+1)
#     secret+=new_char
# print(secret)


# upper ,lower, number 

# write a function to convert vowel char in string to next char
# hello  --> hfllp

# code== ord()
# char==chr()
