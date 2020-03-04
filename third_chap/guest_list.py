guests = ["Prio", "Orpon", "Rokib"]
print(f"{guests[0]} come dinner today")
print(f"{guests[-1]} you are not a guest i think Lol ")
print(f"{guests[1]} come dinner with {guests[0]}")


print(f"{guests[-1]} can't make it today")
guests[-1] = "Annni"
print(guests)
print(f"{guests[0]} come dinner today")
print(f"{guests[-1]} please come to dinner ")
print(f"{guests[1]} come dinner with {guests[0]}")


print("We found a bigger table for you guys!")
guests.insert(0, "Rokib")

guests.insert(2, "Jallu")

guests.append("Rahim")

print(guests)
print(f"{guests[0]} come dinner today")
print(f"{guests[1]} please come to dinner ")
print(f"{guests[2]} come dinner with {guests[0]}")
print(f"{guests[3]} please come to dinner ")
print(f"{guests[4]} please come to dinner ")
print(f"{guests[5]} please come to dinner ")

print("Sorry guys only two seat available for you")
first_guest = guests.pop()
print(f"I'm sorry {first_guest} i can't invite you this time")
second_guest = guests.pop()
print(f"I'm sorry {second_guest} i can't invite you this time")
third_guest = guests.pop()
print(f"I'm sorry {third_guest} i can't invite you this time")
last_guest = guests.pop(2)
print(f"I'm sorry {last_guest} i can't invite you this time")
print(f"{guests[0].title()} and {guests[1].title()} you guys still invited")

del guests[0]
del guests[-1]
print(guests)
print("\nThe number of people i have finally invited is: ")
print(len(guests))

