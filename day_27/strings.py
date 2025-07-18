# ascii -- 
#upper 65-90 
#lower 97-122 
#num 48-57 

# ord() 
#chr() 



# slice:
#slice -- is small portion  of unit
# it can be of different sizes 


# word="preethi"   #pre slice    word  0 1 2 3
##first three characters 
# res=""
# for i in range(3):
#     res+=word[i]
# print(res)

#thi   
# res=""
# for i in range(len(word)-3,len(word)):
#     res+=word[i]

# print(res)
# res=""
# for i in range(2,5):
#     res+=word[i]   
# print(res) 

# word="arundhathi" 
# [::]  ->slicing 
#[start:stop:step]
# string[S:S:S]

# print(word[0:4:1])
# print(word[len(word)-4:len(word):])
# print(word[len(word)-1:-1:-1])

#negitive indexing 0 1....n 
# word="pasupathi"   ##-1 -2 -3  ...-9   
# print(word[-1])  ##last will always be in -1
# print(word[-5]) 
# last=-(len(word))
# print(word[last]) 
# print(word[-1:-10:-1])
# print(word[::-1]) 

# word="markram"
# if (word==word[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")



# print(sub_str in word)
#0-4
#1-5
#2-6
#3-7
# word=input("enter the string: ")
# sub_str=input("enter  the substring: ")
# sub_len=len(sub_str)
# for i in range(len(word)):
#     if word[i:i+sub_len]==sub_str:
#         print(sub_str,"is part of ",word)
#         break

# sentence="my mommmy makes the lunch mom"
# sentence=sentence.split(" ")
# palindrome_exists=False
# for i in range(len(sentence)):
#     if sentence[i][::-1]==sentence[i]:
#         palindrome_exists=True
#         print("there are palindromes")
#         break
# if palindrome_exists==False:
#     print("there are no palindromes") 

#write a function to return the no of palindromes in the string
# sentence=" my family constists of amma nanna akka anna"

# slicing:  extracting a part of the string
#[start:stop:step]
#negitive indexing : -1     -(len(string))