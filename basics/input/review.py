# Read bot data
print("Please enter the number of lives")
lives =int(input())
print("Please enter the energy level")
energy=int(input())
print("Please enter the shield level")
shield=int(input())
# Display bot data
print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)
print ()
health = (lives + energy + shield / 3 )
print("Your total health is:", health, "!")