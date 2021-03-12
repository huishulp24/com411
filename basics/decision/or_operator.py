print("What type of adventure do I take?")
adventure = input()
if( (adventure == "scary") or (adventure == "short") ):
 print("Entering the dark forest!")
elif ( (adventure == "safe") or (adventure == "long") ):
 print("Taking the safe route!")
else:
  print("Not sure what route to take!")