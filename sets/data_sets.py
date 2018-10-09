# Author: Maria Peniche

cars = ['honda', 'toyota', 'bugadi', 'ferrari']
set_one = set(cars)
cars_two = ['bugadi', 'toyota', 'ferrari', 'honda']
set_two = set(cars_two)

def compare(set_one, set_two):
    # if two sets are the same lenght, they must be equal
    if len(set_one) != len(set_two):
        return False
        # Validate that all items in set_one are in set_two
    for item in set_one:
        if item not in set_two:
            return False
    return True
print(compare(set_one, set_two))
