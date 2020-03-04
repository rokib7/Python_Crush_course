places = ["A", "B", "C", "D", "E"]
print("Orginal list:  ")
print(places)

print("\nAlphabetical order: ")
print(sorted(places))

print("\nOrginal list:  ")
print(places)

print("\nReverse Alphabetical order:  ")
print(sorted(places, reverse=True))

print("\nOrginal list:  ")
print(places)

print("\nReversed:  ")
places.reverse()
print(places)

print("\nReversed back to get orginal list: ")
places.reverse()
print(places)

print("\nAlphabetically sorted order: ")
places.sort()
print(places)

print("\nAlphabetically reverse order: ")
places.sort(reverse=True)
print(places)

