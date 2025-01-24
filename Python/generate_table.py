def multi(i):
    t=i 

    with open(f"{t}.txt","w") as f:
        for j in range(1,11):
            # str1=i,"*",j,"=",i*j,"\n"
           
            f.write(f"{i}*{j}={i*j}\n")
        f.close()

for i in range(2,21):
    multi(i)