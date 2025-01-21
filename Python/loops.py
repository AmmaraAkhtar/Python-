#  Write a program to print multiplication table of a given number using for loop. 


# for i in range(1,11):
#     print("9*",i,"=",9*i)


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if(i[0]=='S'):
#         print(i,"greet")



# 3. Attempt problem 1 using while loop. 
# i=1
# while i<=10:
#     print("9*",i,"=",9*i)
#     i=i+1


# 4. Write a program to find whether a given number is prime or not. 



# # Write a program to calculate the factorial of a given number using for loop.

# n=4
# i=1
# fa=1
# while i<=n:
#     fa=fa*i
#     i=i+1


# print(fa)



#  Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3


# for i in range(1,4):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



#  Write a program to print the following star pattern. 
# 
# 7. Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 

for i in range(1,4):
    l=2*i-1 
    if(l==1):
        print("     *")
    if(l==3):
        print("   * * *")    
    if(l==5):
        print(" * * * * *")



# for i in range(1,4):
#     for j in range(1,4,1):
#         if(i==2 and j==2):
#             print(end="  ")
#             continue
#         else:
#             print("*",end=" ")
#     print()
