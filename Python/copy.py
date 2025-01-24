with open("2.txt","r") as f:
    r=f.read()
    with open("des.txt","w") as f:
        f.write(r)