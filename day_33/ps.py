#to find the smallest palindrome in the string 

# word="abcdefghaa"   # markram arakra rkr   rkr
# smallest=word 
# for i in range(len(word)): 
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]  #m
#         if len(temp)>=2 and (temp==temp[::-1] and len(temp)<len(smallest)):
#             smallest=temp
# if smallest!=word:
#     print(smallest)
# else:
#     print("there are no palindromes")     
    
    
    
# word="malayalam"  #malayalam alayala layal aya ala ala
# pali_count=0
# i=0 
# list=[]
# while i<len(word):
#     temp=""
#     for j in range(i,len(word)) : 
#         temp+=word[j] 
#         if temp==temp[::-1] and len(temp)>=2:
#             if temp not in list:
#              list.append(temp)
#              pali_count+=1
#     i+=1
# print(pali_count,list)   




         #    row     col      space
#     *       1       1          4
#    * *      2       2          3
#   * * *     3       3          2
#  * * * *    4       4          1
# * * * * *   5       5          0

#i=1 2 3 4 5   r=5    space?        rows-i 5-1 =4  5-2=3  5-3=2  5-4=1 5-5=0
# rows=5
# for i in range(1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):#1234 
#         res+=" " #"    "
#     for j in range(1,i+1):
#         res+="*"+" " #"    *"    "   * *"   "  * * * " " * * * * " "* * * * *"
#     print(res)
        


         #    row     col      space
#         *     1       1          8
#       * *     2       2          6
#     * * *     3       3          4 
#   * * * *     4       4          2  
# * * * * *     5       5          0   

# rows=5
# for i in range(1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):#1234 
#         res+=" "+" " #"    "
#     for j in range(1,i+1):
#         res+="*"+" " #"    *"    "   * *"   "  * * * " " * * * * " "* * * * *"
#     print(res)


         #     row    col   space   rev
# * * * * *    1       5      0      5
#  * * * *     2       4      1      4 
#   * * *      3       3      2      3
#    * *       4       2      3      2
#     *        5       1      4      1 

#i= 5 4 3 2 1  rows=5  spaces  rows-i  5-5=0  5-4=1  5-3=2 5-2=3  5-1=4

# rows=5 
# for i in range(rows,0,-1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
    
    
    
             #     row    col   space   rev
# * * * * *    1       5      0      5
#   * * * *     2       4      1      4 
#     * * *      3       3      2      3
#       * *       4       2      3      2
#         *        5       1      4      1 

# rows=5 
# for i in range(rows,0,-1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "+" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)



         #    row     col      space
#     *       1       1          4
#    * *      2       2          3
#   *   *     3       3          2
#  *     *    4       4          1
# * * * * *   5       5          0 

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         if i==j or i==rows or j==1 or i==1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)


       #         i       j    spaces
#     *          1       1      4
#    * *         2       2      3
#   * * *        3       3      2
#  * * * *       4       4      1
# * * * * *      5       5      0
#  * * * *       4       4      1
#   * * *        3       3      2
#    * *         2       2      3
#     *          1       1      4


# rows=5
# for i in range(1,rows):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)

# for i in range(rows,0,-1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
    
    

#hour glass pattern 
    
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *