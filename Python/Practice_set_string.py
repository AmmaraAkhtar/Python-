# name=input("Enter the name:")
# print("GOOD AFTERNOON",name)

# name=input("Enter name:")
# Data=input("Enter Data:")
# print(f"Dear <|{name}|>,you are selected!<|{Data}|>")


# string="Ammara  Akhtar"
# print(string.find("  "))
# print(string.replace("  "," "))


# Escape Sequence

# letter="Dear Harry, this python Course is nice. Thanks!"
# print(letter)



letter= ''' 
Dear <|name|>,
             you are selected!
                      <|Data|>
'''
print(letter.replace("<|name|>","Ammara").replace("<|Data|>","19, jan 2025"))