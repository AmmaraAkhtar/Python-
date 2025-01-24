# def function():
#     print("helo",end=" ")
# function()
# print("hello")




# def function(n):
#     if n==1:
#         return 1
#     else:
#         return n+function(n-1)
# print(function(3))



# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

# def function(n):
#     for i in range(1,n+1):
#         for j in range(n,i-1,-1):             1-1=0,2-1=1, 3-1=2
#             print("*",end=" ")
#         print()

# function(3)




# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 


# def function(list,name):
#     list1=[]
#     for i in list:
#         w=i.strip()
#         if(w!=name):
#             list1.append(w)
#     return list1
            
# list=["ammara","asma"]
# name=function(list,"asma")
# print(name)



