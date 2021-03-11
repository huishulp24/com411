print("Where should I look?")
place = input()
if (place == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bedroom_place = input()
    if (bedroom_place == "under the bed"):
        print("Found some shoes but no battery")
    else:
      print("Where should I look?")
      place = input()
      if(place == "in the bathroom"):
       print("Where in the bathroom should I look?")
       bathroom_place = input()
       if(bathroom_place == "in the bathtube"):
        print("Found a rubber duck but no battery")
      else:
        print("I can not find anything!")
else:
  print("I found it!")
