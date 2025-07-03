#strings methods 
# upper 
# lower 
# captialize 
# title 
# strip 
# lstrip 
# rstrip 
# replace 
# count 
# find
# sen="hello world"
# # print(sen.find("l"))
# c="l"
# for i in range(len(sen)):
#     if c==sen[i]:
#         print(c,"is present in",i)


#count 
# print(sentence.count("ing"))
# sentence="aishwarya"  #ishwry
# for i in range(len(sentence)):
#     if sentence.count(sentence[i])>1:   ##aishwarya.count(a) 3
#         print(sentence[i])
    

# name="sai"
# print(name.startswith("sai")) 
# name="rakeSH"
# print(name.endswith("sh"))

#isalpha 
# name="rakesh"
# print(name.isalpha())


# mob="9848022338"
# print(mob.isdigit())

# user_id="raki123"
# user_id="raj"
# user_id="123456"
# print(user_id.isalnum())


# word="PythoN"
# # print(word.swapcase())
# for c in range(len(word)): #0 1 2 3 4 5 
#     if word[c]==word[c].upper():  ##word[0]  == word[0].upper() P==P y==Y t==T h==H o==O N==N
#         print(word[c].lower()) #p n
#     else:
#         print(word[c].upper()) #Y T H O
    

# word="sai"
# word="programming language"
# print(word.zfill(15))
# name="panduranga rao garu"
# l=15
# req=l-len(name) #15-19 -4 
# new_str=""
# for x in range(0,req): #0 -4
#     new_str+="0"
# print(new_str+name) #""+name  name


# word="i woke up, i went to class"

# print(word.split(" "))  ##it will return a list 

# num_list=["hi","how","r","u","?"]
# print(" ".join(num_list))

# word="koushik"#["k","o"...."k"]
# word=word.split(" ")
# print(word)


#palindrome 
# word="cat"  #
# rev=""
# for z in range(len(word)-1,-1,-1):
#     rev+=word[z]  ##malayalam   
# if rev==word:
#     print("palindrome")
# else:
#     print("not palindrome")

