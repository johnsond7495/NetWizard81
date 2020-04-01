# This program uses primary colors to determine the secondary colors.
# CTI-110
# P3HW1 - Color Mixer
# 31 March 2020
# Johnson Devorick

p1 = input('Enter primary color 1 ')
p2 = input('Enter primary color 2 ')

if p1 == 'red' and p2 == 'blue':
    print('When you mix red and blue, you get purple.')

elif p1 == 'blue' and p2 == 'red':
    print('When you mix blue and red, you get purple.')

elif p1 == 'red' and p2 == 'yellow':
    print('When you mix red and yellow, you get orange.')

elif p1 == 'yellow' and p2 == 'red':
    print('When you mix yellow and red, you get orange.')

elif p1 == 'blue' and p2 == 'yellow':
    print('When you mix blue and yellow, you get green.')

elif p1 == 'yellow' and p2 == 'blue':
    print('When you mix yellow and blue, you get green.')
    
