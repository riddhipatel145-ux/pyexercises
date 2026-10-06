"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of eight monthly procurement budgets from Exercise 4.0.
# 2. Process: Go through each budget and compare it with $12000.
# 3. Out: One line for each budget showing its position, amount and whether it is above or beloe $12000.
# 4. What I compute for each item, and why it is worth showing: I compute if each budget is above or below $12000.


# Your code below

budgets = [12000, 9500, 15000, 11000, 13500, 10000, 16000, 12500]

for position, budget in enumerate(budgets, start=1):
    if budget >= 12000:
        print(position, budget, "Above or equal to $12000")
    else:
        print(position, budget, "Below $12000")