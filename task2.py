# Task 2
# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters. 
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. 
# Make the function print out the values of the dictionary to make sure that it works as intended.


def make_country(**countries):
 for сountry,capitals in countries.items():
        print(f'{сountry} - {capitals}')
make_country (Czech_Republic = "Prague", Italy = "Rome" , France  = "Paris" , Hungary = "Budapest" )