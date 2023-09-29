weight=int(input("Weight: "))
unit=input("(L) or (K): ")
if(unit.upper()=="L"):
   converted= weight*0.45
   print(f'you are {converted} Kilos')
elif(unit.upper()=="K"):
    converted=weight/0.45
    print(f'you are {converted} pounds')

