with open("python.txt","r") as f:
    a=f.readline()
    l=1
    while(a!=" "):
        if("python" in a):
            print("line no:",l)
        a=f.readline()
        l=l+1