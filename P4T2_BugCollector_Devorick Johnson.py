# This program tracks how many bug are collected for 5 days.
# CTI-110 P4T2 - Bug Collector
# Devorick Johnson
# 15 April 2020

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 5):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total = total + bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
