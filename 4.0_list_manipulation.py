"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight monthly procurement budgets.
# 2. Process: Create the list, diplay it, choose one budget, sort the list, and calculate the total.
# 3. Out: The complete list, one budget, the sorted list, and the total budget.
# 4. What my list is about, and what I computed from it: My list is about monthly procurement budgets. I computed the total because it shows the overall budget for the eight months. 


# Your code below
# Cretae a list of monthly procurement budgets.
list1 = [1200, 1500, 1100, 1800, 1400, 1600, 1300, 1700]

print(list1)

# Choose one budget from the list.
num = list1[5]

print(num)

# sorting the list.
sorted_list = list1.sort()

print("The sorted list is:", list1)

# Calculate the total of the budgets.
total = sum(list1)

print("The total budget is:", total )