print ("Welcome to SMIT TechFest!")
print ("Organized by Juaquin Luis T. Valladolid of APPDAET BTCS2\n")

register = input("How many participants will register?: ")
if register <= "0":
    print("Invalid number of Participants.")
    exit()
else:
    register = int(register)

participants = []
for i in range(register):
    name = input("Enter Participant Name: ")
    track = input ("Enter Chosen Track: ")
    participants.append({"name": name,"track": track})


print("Registered Participants:")

for p in range(len(participants)):
    print(f"{p +1}. {participants[p]["name"]} - {participants[p]["track"]}")