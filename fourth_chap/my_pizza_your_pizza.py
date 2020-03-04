fav_pizza = ["cheese", "hawaiian", "mushroom"]

frnd_pizza = fav_pizza[:]

fav_pizza.append("Chilli")
frnd_pizza.append("Nopizza")

print("My fav pizza are: ")
for pizza in fav_pizza:
    print(pizza)

print("\nMy frnd's fav pizza are:")
for pizza in frnd_pizza:
    print(pizza)

