import random
guesser=0
toGuess=0
attempts=0
print("How Many Digit Guesser Would you like?(1-5)")
dig = int(input("Enter Your Number here: "))
if dig ==1:
    toGuess=random.randint(0,9)
elif dig==2:
    toGuess=random.randint(0,99)
elif dig==3:
    toGuess=random.randint(0,999)
elif dig==4:
    toGuess=random.randint(0,9999)
elif dig==5:
  toGuess=random.randint(0,99999)
else:
    print("Please input a valid Integer(1-5)")
    dig = int(input("Enter Your Number here: "))
while guesser!= toGuess:
    attempts+=1
    print("try Guessing The "+str(dig)+" digit number")
    guesser = int(input("Enter Your Number here: "))
    if toGuess>guesser:
        print("Value is too low")
    elif toGuess<guesser:
        print("Value is Too Large")

print("Congrats! It Took You "+str(attempts)+" Attempts!")

