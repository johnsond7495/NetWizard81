# This program creates a step pattern
# 16 April 2020
# CTI-110 P4HW3 - Nested Loops
# 16 April 2020
# Devorick Johnson

NUM_STEPS = 6

for r in range(NUM_STEPS):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')

