# This program gives the user the option to add or substract the giving numbers.
# 19 April 2020
# CTI-110 P5HW2 - Math Quiz
# Devorick Johnson




import random

randomNum1 = random.randint( 1, 250 )
randomNum2 = random.randint( 1, 250 )

def askQuestion():
    global randomNum1
    global randomNum2
    userAnswer = int( input('What is ' + str( randomNum1 ) + ' + ' + \
                            str( randomNum2 ) + '?: ') )
    return userAnswer

def checkAnswer( userAnswer ):
    global randomNum1
    global randomNum2

    correctAnswer = randomNum1 + randomNum2
    print()
    if userAnswer == correctAnswer:
        print( 'Congratulations!' )
    else:
        print( 'Its wrong. Correct answer is', correctAnswer )

def main():
    userAnswer = askQuestion()
    checkAnswer( userAnswer )

main()

    
print('MAIN MENU')
print('1.Add')
print('2.Subtract')
print('3.Exit')

choice = input('Select a option from the Menu" ')

if choice == '1':
    print(randomNum1, '+', randomNum2, '=', add(randomNum1,randomNum2))

if choice == '2':
    print(randomNum1, '-', randomNum2, '=', substract(randomNum1,randomNum2))

elif choice == '3':
    print('Program has Exit')
