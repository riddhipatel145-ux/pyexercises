"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in? 
    2. What happens to it? 
    3. What comes out? 
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number N entered by the user
# 2. Process: check every number from 1 to N and determine whether each one is odd or even
# 3. Out: Each number from 1 to N with a message saying whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number: for 0 or a negative number, display a message that N must be greater than 0. For a very Large number such as 5000, display a message that the number is too large.


# Your code below
# Ask the user to enter a number. 
num = int (input("Enter a number: "))

# Check if the number is valid and not too large.
if num <= 0:
    print("Please enter a number greater than 0.") 
elif num > 100:
    print("The number is too large.")
else:
    # Check every number from 1 to the user's number.
    for i in range(1, num + 1):
        # Check if the number is even or odd.
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")