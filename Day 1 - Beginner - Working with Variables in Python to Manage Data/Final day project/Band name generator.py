## Simple project demonstrating the concatenation of two strings, and taking input from user ##


#formatting purposes
print("\n")

# printing introduction + asking user for input. (end parameter is to not let print function jump to a new line and instead remain on the same line)
print("Welcome to the Band Name Generator.\n")

#taking city input from user
city = input("What's the name of the city you grew up in? ")

#taking pet nanme from user
pet = input("\nWhat's your pet's name? ")

#concatenating city and pet names to produce a band name
print(f"\nYour band name could be {city + ' ' + pet}")

