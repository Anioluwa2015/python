med=input("are you sick? yes or no:")
attendance=int(input("what is your attendance:"))

if med == "yes":
    print("your allowed")
else:
    if attendance > 75 :
        print("you are allowed")
    else:
        print("you are not allowed")