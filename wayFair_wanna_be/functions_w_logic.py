# Author: Maria Peniche

# Depending on the order amount,
# our user might get free shipping,
# so the print statement is different.

# build a function that works for any product and order_amount

# product = []
# order_amount = 35

def order_checkOut(product, order_amount):
    print("Thank you for ordering", product, "come visit Wayfair for all your home needs!")
    if order_amount >= 30:
        print("It's your lucky day! There is no shipping charge for orders over $30.00.")
    else:
        print("There will be a $5.00 shipping charge for this order.")



order_checkOut("love seat", 18)
