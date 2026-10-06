"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about one product.
# 2. Process: Store the product information in a dictionary, read it, change one field, remove one field, and display all the fields.
# 3. Out: The product information with the changes displayed.
# 4. My object, my five fields, and why those: My object is a product. I chose name. price, category, brand, and stock because these are useful information about a product.


# Your code below
product = {
    "name": "Chocolate",
    "price": 2.50,
    "Category": "Food",
    "brand": "Lindt",
    "stock": 20
}

# Read a field
print("Product name:", product["name"])

# Change a field
product["price"] = 3.00

# Remove one field
del product["stock"]

# Ask for a field that does not exit 
print("Color:", product.get("color", "Field does not exist"))

# Display every field with its value
for field, value in product.items():
    print(field, ":", value)