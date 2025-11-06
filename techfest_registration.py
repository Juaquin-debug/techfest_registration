print ("Welcome to SMIT TechFest!")
print ("Organized by Juaquin Luis T. Valladolid of APPDAET BTCS2\n")

participants = input("How many participants will register?: ")
if participants <= "0":
    print("Invalid number of Participants.")
    exit()
else:
    participants = int(participants)

for participant in range(participants):
    name = input("Enter Participant Name: ")
    track = input ("Enter Chosen Track: ")