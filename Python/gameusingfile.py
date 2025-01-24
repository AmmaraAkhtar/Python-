import random



def game():
    user=random.randint(1,150)
    with open("game.txt","r") as f:
        a=f.read()
        b=int(a)
    if(b<user):
        print("user score:",user)
        user=str(user)
        with open("game.txt","w") as f:
            f.write(user)
    else:
        print("not need to update")
    
game()



