age = 17
if age < 4:
    # print("Your admission cost is $0")
    price = 0
elif age < 18:
    # print("Your admission cost is $25")
    price = 25
elif age < 64:
    price = 40
else:
    # print("Your admission cost is $40")
    price = 20
print(f"Your admission cose is ${price}.")

