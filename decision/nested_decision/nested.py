# ask user what to do
print("What should I do (play/study)?")
activity = input()
if(activity == "play"):
  print("What should I play with(toy/friend)?")
  play_with = input()
  if(play_with == "toy"):
    print("I will play with toys!")
  else:
    print("I will play with my friend!")
else:
  print("I will study!")