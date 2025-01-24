with open("2.txt","r") as f:
    r=f.read()
    with open("des.txt","r") as w:
        l=w.read()
        if(r==l):
            print("same content")
        else:
            print("not same")



        