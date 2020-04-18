# This program converts feet to inches.
# 18 April 2020
# CTI-110 P5T2_FeetToInches
# Devorick Johnson


# Represents the number of inches per foot.
INCHES_PER_FOOT = 12

# This is the main function.
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Conver that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# This is the function converting feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
