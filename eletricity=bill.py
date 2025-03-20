eletricity=int(input("please enter the units you use:"))

if eletricity <= 50:
    amount=eletricity*2.50
    
elif eletricity <100:
    amount=eletricity*4.5

else:
    amount=eletricity*8.2

print(amount)    