command=""
started=False
while(True):
    command=input(">").lower()
    if(command=="help"):
        print("""
start-> car started and ready to go
stop->car stopped
quit->quit the game        
        """)
    elif(command=="start"):
        if started:
            print("car is already started what are you doing")
        else:
            started=True
            print("car started...")

    elif(command=="stop"):
        if not started:
            print("already stopped")
        else:
            started=False
            print("car stopped.")

    elif(command=="quit"):
        break
    else:
        print("Sorry,i don't understand")