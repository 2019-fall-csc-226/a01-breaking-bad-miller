######################################################################
# Author: Dakota Miller      TODO: Change this to your name
# Username: millerd2            TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
birth_year = int(input("What is your birth year"))
print(birth_year)

if birth_year == int(1999):
    print("You are a rabbit, You must be fast.")
if birth_year == int(2000):
     print("Wow you are a DRAGON!")
if birth_year == int(2001):
    print("You are a snake, scary.")
if birth_year == int(2002):
    print("You are a horse, do you trot?")
if birth_year == int(2003):
    print("What a Goat")
if birth_year == int(2004):
    print("You are a monkey, do you like monkeying around?")
if birth_year == int(2005):
    print("You arr a rooster, are you a early riser?")
if birth_year == int(2006):
    print("You are a dog, woof.")
if birth_year == int(2007):
    print("You are a pig, oink oink.")
if birth_year == int(2008):
    print("You are a rat, eww.")
if birth_year == int(2009):
    print("You are an ox, are you strong?")
if birth_year == int(2010):
    print("You are a tiger, that's cool.")
if birth_year == int(2011):
    print("You are a rabbit, are you fast?")
# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
buddies = int(input("Hey buddy what is your birth year?"))
print(buddies)
if buddies == int(2000):
    print("You are a dragon, thats crazy dude!")
else: print(" You aren't my friend.")


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
