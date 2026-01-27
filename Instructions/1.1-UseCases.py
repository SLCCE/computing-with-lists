# people in a line
people = ["Alice", "Bob", "Carol"]
print(people)
# items for a restaurant order
order = ["Steak", "Carrots", "Dinner Roll"]
print(order)
# store inventory
inventory = ["Apple", "Orange", "Cereal"]
print(inventory)

# I want an apple but I currently have an orange. Help me get one!
item = inventory[1]
print("I have a", item)

# what happens if we try to access something out of bounds?
#    0    1    2
b = ["a", "b", "c"]
x = b[3]
print(x)

# negative indexing
x = b[-1]
print(x)
