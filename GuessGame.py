number=8
guess_count=0
guess_limit=3
flag=False
while guess_count<guess_limit:
    Guess=int(input("guess: "))
    guess_count+=1
    if(Guess==number):
        print("you Won !")
        break
else:
  print("you failed to guess")