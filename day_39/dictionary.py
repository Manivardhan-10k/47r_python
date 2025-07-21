# string number  
#list 
#dictionary
# {key:value} 

# details=["mani",25,"hyd",99] 
# details={
#     "age":25,
#     "city":"hyd",
#     "marks":99,
#     "emp":True,
#     "name":"mani",
# }
# # print(details[0])
# #CRUD  create read update delete 
# print(details["emp"]) 
# print(details["marks"]) #99
# details["marks"]=100 
# print(details["marks"]) #100 


#get 
# company={
#     "google":"sundar pichai",
#     "apple":"tim cook",
#     "twitter":"musk",
#     "meta":"zuckerberg",
#     "microsoft":"satya nadella", 
#     "amazon":"jeff bezos"
# }  
# val=company.get("google")
# print(val)
# print(company.get("amazon")) 
# print(company["amazon"])   

#keys 

# print(company.keys()) 

# if "amazon" in company.keys():
#     print("there is a key")
# else:
#     print("there's no key")


# print(len(company)) 


#values 

# print(company.values())

# print(company.items()) 

# for i in company.items():
#     if "google" in i:
#         print(i) 



# places={
#     "hyd":"biryani",
#     "gnt":"chilli",
#     "kkd":"sweet",  
# } 
# places.update({"kkd":"kaja"})
# print(places) 
# places["kkd"]="kaja"
# print(places)  
# places.pop("gnt")
# print(places)   

# places.popitem()
# print(places)    

# places["tpt"]="laddu"
# print(places)


#get keys values items update pop popitem setdefault  

# places.clear()
# print(places)



# marks={
#     "bhargav":100,
#     "bhaskar":83,
#     "anvesh":108,
#     "mounika":85,
#     "kalyani":87
# }

# ##sum  of marks/no of students 
# total=0
# count=0
# for i in marks:
#     total+=marks[i]
#     count+=1
# print(total/count) 


# student={
#     "name":"bhargav",
#     "marks":[35,90,72,55,61,39]
# }
    
# total=sum(student["marks"])
# print(total)
# student["total"]=total 
# print(student)