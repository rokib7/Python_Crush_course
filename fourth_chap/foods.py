my_food = ["pizza", "falafel", "carrot cake"]
friend_foods = my_food[:]
# friend_foods = my_food // this doesn't work for both list with append

my_food.append("Milk")
friend_foods.append("Banana")

print("My favourite foods are: ")
print(my_food)
print("\nRunning this avobe my_food in loop: ")
for food in my_food:
    print(food)

print("\nMy Friend's fav foods are: ")
print(friend_foods)
print("\nRunning this avobe friend_foods in loop: ")
for food in friend_foods:
    print(food)

