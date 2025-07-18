# * * * * *    0 5  5
#  * * * *     1 4  4
#   * * *      2
#    * *       3
#     *        4
#    * *       3 2 2
#   * * *      2 3 3
#  * * * *     1 4 4
# * * * * *    0 5 5


# rows=5 
# for i in range(rows,0,-1):
#     res="" 
#     for space in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)

# for i in range(2,rows+1):#2 3 4 5 
#     res=""
#     for space in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)
    
    
    
    
    
     #          i       j       spaces
#     *         1       1        4
#    * *        2       2        3
#   * * *       3       3        2
#  * * * *      4       4        1
# * * * * *     5       5        0
#  * * * *      6       4        1
#   * * *       7       3        2
#    * *        8       2        3
#     *         9       1        4

# rows=5  

#i<=rows  rows-i 
#i= 6 7 8 9  rows=5           6-5=1  7-5=  2  8-5=  3  9-5=  4

#i<=rows    i 
#i=6 7 8 9  rows=5      2*5-6= 4   2*5-7=3   2*5-8=2   2*5-9= 1

# for i in range(1,2*rows):
#     res=""
#     spaces= rows-i if i<=rows else i-rows
#     cols= i if i<=rows else 2*rows-i
#     res+= (" "*spaces )+ ("* "*cols)
#     print(res)




      
      #       sp j  i
# * * * * *    0 5  1
#  * * * *     1 4  2
#   * * *      2 3  3
#    * *       3 2  4
#     *        4 1  5
#    * *       3 2  6
#   * * *      2 3   7 
#  * * * *     1 4   8  
# * * * * *    0 5   9   

# rows=5   
#i<=rows  i-1 
#i= 6 7 8 9    rows=5        2*5-6-1=3     2*5-7-1= 2     2*5-8-1=1    2*5-9-1= 0 


#i<=rows   rows-space 
# rows-space

# for i in range(1,2*rows):
#     spaces= i-1 if i<=rows else 2*rows-i-1 
#     cols= rows-spaces 
#     print((" "*spaces)+"* "*cols) 


#     a
#    b c 
#   d e f
#  g h i j 
# k l m n o 
#  p q r s 
#   t u v 
#    w x 
#     y  

# rows=5
# code=97 
# for i in range(1,2*rows):
#     res=""
#     spaces= rows-i if i<=rows else i-rows 
#     res+=" "*spaces
#     cols= i if i<=rows else  2*rows-i
#     for j in range(cols):
#         res+=chr(code)+" "
#         code+=1      
#     print(res)


# word="aaaaaaaaaaaaaa"
# longest=""
# char=word[0]
# if word.count(char)==len(word):
#     longest=char
# else:
#     for i in range(len(word)):
#       temp=""
#       for j in range(i,len(word)):
#         if word[j] in temp:
#             break 
#         else:
#             temp+=word[j]
#             if len(temp)>len(longest):
#                 longest=temp       
# print(longest) 




#CNSITEZH 
# *       * 
#   *   * 
#     * 
#   * 
# *

# *       * 
#   *   * 
#     * 
#     * 
#     * 

# *       *
# * *   * *
# *   *   * 
# *       *
# *       * 


# word="aaaaabbccaabbcc" 
# i=0
# while i<len(word):
#     count=1
#     temp=""
#     for j in range(i,len(word)-1):
#      if word[j+1]==word[j]:
#         temp+=word[j]
#         count+=1 
#      else:
#          break
#     i+=count
#     print(word[j],count)
    
    