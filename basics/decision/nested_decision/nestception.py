print("Where should I look?")
place = input()
if(place == "in the bedroom"):
  print("Where in the bedroom should I look?")
  bedroom_place = input()
  if(place == "in the cupboard"):
    print("Found some mess but no battery.")
  else:
      print("Where should I look?")
      place = input()
      if(place == "in the bathroom"):
       print("Where in the bathroom should I look?")
       bathroom_place = input()
       if(bathroom_place == "in the bathtube"):
        print("Found a rubber duck but no battery")
      else:
        print("Where should I look?")
        place = input()
        if(place == "in the lab"):
         print("Where in the lab should I look?")
         lap_place = input()
         if(place == "on the table"):
          print("Yes! I found my battery!")            
        
