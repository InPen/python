#Author: Maria Peniche

# Unit 1

movie_titles = ['Aaladin', 'Hercules', 'ALL Harry Potter Movies', 'Frida']
movie_ratings = 8
# print("The movie", movie_titles, "is ", movie_ratings)
# print("The movie " + str(movie_titles) + " is " + str(movie_ratings))

# Unit 2

# musicians = {'guitar': 'robby', 'vocals': 'john lennon', 'bass': 'john paul jones', 'drums': 'bill ward'}
#
# for instrument, musician in musicians.items():
#   print("Now introducing {0} on the {1}, they {2}".format(musician, instrument, 'ROCK'))

def print_rating(movie_title):
    for movie_title in movie_titles:
        print(movie_title)

print_rating(movie_titles)

def print_all_ratings(movie_titles):
    print('The rating for', movie_title, 'is', movie_ratings)

    # mode

    # If mode is equal to search, your app will
    # then print ('Back To The Future', 'Blade', 'Spirited Away')

    # If mode is equal to ratings, your app will
    # then print('The rating for Back To The Future is 8.')
    # pass
    # print('hello')












# this is the main function that will be invoked at the end of the file
# def main():


# dunder main
# if __name__ == "__main__":
#  main()
