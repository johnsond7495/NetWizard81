# This program calculates Expense
# CTI-110 P4HW1 - Expenses
# Devorick Johnson
# 15 April 2020

another = 'y' #Variable to control loop.

# Initialize accumu100lator variable
total = 0
entry = 2
    
# Get the expense amount
for number in range(1, 2, 3,):
    print('Enter starting amount in account?' )
    number = int(input())

    print('Enter Expense 1' )
    expense = int(input())
    total = number - expense

another = input('Do you want to enter another expense (y/n:) ')

# Display the total expense.
print('Your expense is', total)

# Ask user if he/she need to enter another expense

if another == 'y':
    print('Enter expense 2' )
    expense2 = int(input())
    total2 = total - expense2

another = input('Do you want to enter another expense (y/n:) ')
if another == 'n':

    print('Amount in account before expense substration', number )

    print('Number of expenses entered:', entry )

print('Amount in account AFTER expenses substracted', total2)






