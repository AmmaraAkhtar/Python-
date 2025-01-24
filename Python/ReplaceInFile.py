# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 

with open("donket.txt","r") as f:
    a=f.read()
    print(type(a))
    if "donkey" in a:
         print("donkey in file")
         a=a.replace("donkey","#####")
         with open("donket.txt","w") as f:
              f.write(a)
              
    else:
         print("not present")
         

    # while(a!=" "):
    #     if("donkey" in a):
    #         print("donkey in file")
    #     else:
    #         print("not present")
    #     a=f.readline()
    
    
