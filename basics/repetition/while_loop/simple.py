print("How many cables should I remove?")
cables_to_remove =int(input())
removed = 0

while( removed < cables_to_remove ):
  print("Removing...", end ="")
  removed = cables_to_remove + 1
print("Done!", removed, "cables")
