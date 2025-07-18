#matrices 

#add 
#sub 
#mul 

#rows and cols should be the same 


# mat1=[
#     [1,2,3],
#     [4,5,6],

# ]
# mat2=[
#     [7,8,9],
#     [10,11,12]
# ]
# possible=True
# if len(mat1)==len(mat2):
#     for i in range(len(mat2)):
#         if len(mat1[i])!=len(mat2[i]):
#             possible=False 
#             break 
# else:
#     possible=False
# if possible:
#     print("both matrices have same dimensions") 
# else:
#     print("both matrices dont have same dimensions")  
    
    
# mat1=[
#     [1,2,3],
#     [4,5,6],

# ]
# mat2=[
#     [7,8,9],
#     [10,11,12]
# ] 

# out=[
    
#     [8,10,12],
#     [14,16,18]
# ]
# out=[] 
# for i in range(len(mat1)):  #0 1
#     row=[]
#     for j in range(len(mat1[i])): #0 1 2    
#         sum=mat1[i][j]+mat2[i][j]  # 8
#         row.append(sum) #[8,10,12]
#     out.append(row)
# print(out)


#multiplication
        
    

mat1=[
    [5],       ## mat1[0][0]*mat2[0][0]+  mat1[0][1]*mat2[1][0]
    [1]   
]   
mat2=[          ##mat1[0][0]*mat2[0][1] + mat1[0][1]*mat2[1][1] 
    [4,3],    # mat1[1][0]*mat2[0][0]+  mat1[1][1]*mat2[1][0]
    #[9,7]      #mat1[1][0]*mat2[0][1]+  mat1[1][1]*mat2[1][1]
]    


# out=[[92,71],[22,17]]
rows=len(mat1)  
possible=True   
for i in mat2:#[4,3]
    if len(i)!=rows:
        possible=False
        break 
print(possible)
out=[]
#rows *cols  
# for i in range(len(mat1)): #0 1 
#     row=[]
#     e1=0 
#     e2=0
#     for j in range(len(mat2[0])): #1 0
#         e1 = (mat1[i][i]*mat2[i][i])+ (mat1[i][j]*mat2[j][i]) 
#         row.append(e1)
#     # for j in range(len(mat2)-1,-1,-1):
#     #     e2= (mat1[i][i]*mat2[i][j])+(mat1[i][i]*mat2[j][j])
#     #     row.append(e2)
#     out.append(row)
# print(out)

for i in range(len(mat1)):
    row = []
    for j in range(len(mat2[0])):
        s = 0
        for k in range(len(mat1[0])):  # or len(mat2)
            s += mat1[i][k] * mat2[k][j]
        row.append(s)
    print(row)
        
        
    
        
    

