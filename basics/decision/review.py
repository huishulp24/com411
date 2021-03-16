
print("How many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

# Display grid
for row in range(0, rows, ):
  print()
  for column in range(0, columns, ):
    print(":-)", end="")
print()

