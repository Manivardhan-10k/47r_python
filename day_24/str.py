#string 
# collection of characters enclosed in '' ," " , ''''''  or """"""
# '' or "" 
# """""" ''''''
# "bhargav is a 'good' boy"


# sentence="bhargav is a 'good' boy"  #a a i a o o o
#index values - starting from 0 to len(string)

# for i in range(len(sentence)):
#     c=sentence[i] 
#     if c!="a" and c!="e" and c!="i" and c!="o" and c!="u" and c!=" ":
#         print(c , " is in ", i, "index") 
        


# string methods
# print()
# len()
# input()

##there are predefined methods for strings
# word="silent"
# #upper 
# word2=word.upper()  #SILENT 
# print(word,word2)

# word="LISTEn"
# word2=word.upper()
# print(word2)


#lower 

# word="JunO"
# word2=word.lower()
# print(word,word2)


# name="lavanya"
# name=name.capitalize()
# print(name)

# sentence="royal challengers bengaluru has won this year ipl"
# sentence=sentence.title()
# print(sentence)



#strip **
# username=input("enter your name: ")
# username=username.strip()
# print(username,len(username))
# print(username=="mani vardhan")


# user="       python      "

# user=user.lstrip()
# print(user,len(user))
# user=user.rstrip()
# print(user,len(user))

# word="hello people, people are good!" 
# word=word.replace("p","world")
# print(word)

# word="the python is too good"
# print(word.find("t"))

#count 
# sentence="     we are going to play cricket on sunday and have lunch after         "
# spaces=sentence.strip().count(" ")
# print("there are" ,spaces+1,"words")

# char=input("enter the char: ")
# if char==char.upper():
#     print("char is in upper case")
# else:
#     print("char is in lower case")



# sentence="i am learning PYTHON" 
# upper_count=0
# for i in range(len(sentence)):
#     if sentence[i]==sentence[i].upper() and sentence[i]!=" ":
#         upper_count+=1
# print(upper_count)


# sentence="i am learning PYTHON" 

# for index in range(len(sentence)):
#     c=sentence[index] 
#     if (c=="a" or c=="e" or c=="i" or c=="o" or c=="u") and (index%2==0):
#         print(c,index)
    
    
# take string and  a number 
# and return the chars in the multiple of num



