# Author: Maria Peniche

# LIST ITERATIONS

# my_list = ['snooky', 'johann', 'marine', 'itzel']
#
# for love in my_list:
#     print('Hello there ', love)

# LOOPS

# Create a list of colors.
# colors = ['blue', 'gold', 'burgandy', 'violet', 'white']
# Using a for loop, print out the list.
# Using range, set each item in the list to be the number of characters in the color.
# for color in range(len(colors)):
# Print the list
    # print(color)

# WHILE LOOPS

# glass_content = 3
# glass_maximum = 2
#
# while glass_content < glass_maximum:
#     print(glass_content)
#     glass_content +=1


# FUNCTIONS

# my_number = 2

# def high_low():
#     if my_number > 10:
#         print('high!')
#     else:
#         print('low')
# high_low()


# TEMPERATURE LOOP ACUMULATOR

temperature = 90
counter = 0
while True:
    if temperature > 75:
        print:("Temeprature is", temperature, "cranck the AC!")
        temperature -= 3
    else:
        counter += 1
        if counter ==5:
            print:("Temeprature is", temperature, "and raising")
            temperature +=1
            counter = 0
            print("aah, that's better")
