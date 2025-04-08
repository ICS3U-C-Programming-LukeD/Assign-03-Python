#!/usr/bin/env python3

# Created By: Luke Di Bert
# Date: March, 2025

# adds math library
import math


def main():
    # fixed speed limit
    speed_limit = 60

    # Gets speed and displays intro message
    speed = input(
        "The speed limit in the zone is 60 km/h, What is your current speed? (km/h): "
    )
    # Try catch used in order to catch errors
    try:
        # Gets speed, and checks if user is over speed limit
        speed = int(speed)

        # Calculates the amount over the speed limit
        over_speed = speed - speed_limit

        # Defines fine for later calculations
        fine = 0

        # Calculates fine and message depending on users speed
        if speed <= speed_limit:
            print("You are within the speed limit. Good job!")
        elif 1 <= over_speed <= 20:
            print("Warning! Please slow down.")
        elif 21 <= over_speed <= 30:
            fine = over_speed * 4.50
            print("Your fine is $" + str(fine))
        elif 31 <= over_speed <= 50:
            fine = over_speed * 7
            print("Due to higher speeds your fine is $" + str(fine))
        else:  # over_speed > 50
            print("Due to extreme speeds your license has been suspended for 30 days.")

        # Nested if statements that display different outro messages depending on your speed before
        if over_speed:
            if over_speed <= 0:
                print("Thanks for being a safe driver!")
            else:
                if over_speed <= 20:
                    print("Remember, even small speeding can be dangerous!")
                else:
                    if over_speed <= 30:
                        print("Pay attention to speed signs next time!")
                    else:
                        if over_speed <= 50:
                            print("You were going way too fast slow down next time!")
                        else:
                            print("That was reckless driving! Be careful.")

    # Catches non integer input and displays message
    except:
        print(speed, "wasn't a valid integer")

    # Program outro message
    finally:
        print("Thank you for using this program")


if __name__ == "__main__":
    main()
