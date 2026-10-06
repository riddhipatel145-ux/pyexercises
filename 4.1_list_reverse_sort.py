"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of eight monthly procurement budgets from Exercise 4.0.
# 2. Process: Create different orders of the list while keeping the original list unchanged.
# 3. Out: The list in four different orders and the original list at the end.
# 4. My four orders, and which ones modify the original: Ascending order, descending order, reversed order, and a copied sorted order. Sorting with sort() and reversing with reverse() modify the original list, while sorted() and slicing create a copy. 


# Your code below
# Original list from Exercise 4.0
budgets = [12000, 9500, 15000, 11000, 13500, 10000, 16000, 12500]
print("Original list:", budgets)

original_budgets = budgets.copy()

ascending = sorted(budgets)
descending = sorted(budgets, reverse=True)
reversed_budgets = budgets [::-1]
copied_sorted = sorted(budgets)

print("Ascending order:", ascending)
print("Descending order:", descending)
print("Reversed order:", reversed_budgets)
print("Copied sorted order:", copied_sorted)

print("Original list at the end:", budgets)

print("Original list unchanged:", budgets == original_budgets)