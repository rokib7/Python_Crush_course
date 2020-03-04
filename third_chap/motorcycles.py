motor = ["Honda", "suzuki", "cbr"]
print(motor[0].title())
motor[2] = "ducati"
motor.append("Uber")
print(motor)

# adding iteam to a empty list
cigg = []
cigg.append("Benson")
cigg.append("Goldleaf")
cigg.append("hollywood")
cigg.append("marlboro")
cigg.append("benson_switch")
print(cigg)

# inserting iteam from list

condom = ["Durex", "sensation", "raja"]
condom.insert(2, "u_and_me")
print(condom)


# deleting element from a list

name = ["a", "b", "c"]
del name[2]
print(name)

# removing iteam using pop method
condom = ["Durex", "sensation", "raja"]
print(condom)
popped_name = condom.pop()  # poopping from last position
print(popped_name)
popped_name = condom.pop(1)
print(popped_name)

# removing by knowing value but not position

condom = ["Durex", "sensation", "raja"]
# condom.remove("Durex")
# print(condom)
too_expensive = "Durex"
condom.remove(too_expensive)
print(f"\nA {too_expensive.title()} is expensive for me.")
