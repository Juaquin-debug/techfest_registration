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

unique = {p["track"] for p in participants}

print("\nTracks Offered in this Event:")
if len(unique) < 2:
    print("Not enough variety in tracks.")
else:
    print(", ".join(unique))

seen = set()
duplicate = set()
for p in participants:
    if p["name"] in seen:
        duplicate.add(p["name"])
    else:
        seen.add(p["name"])

if duplicate:
    for name in duplicate:
        print("\nDuplicate name found: " + name)
else:
    print("\nNo duplicate names.")