#  Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
#  The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
       
       if discount_percent >= 20:
              return price *(1 - discount_percent/100)
       else:
              return price 
       
       print(calculate_discount(100, 25))  # Output: 75.0
       print(calculate_discount(200, 10))  # Output: 200.0

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
#  Print the final price after applying the discount, 
# or if no discount was applied, print the original price.


OrigignalPrice = float(input("Enter the price of the Item"))

discount_percent = float(input("Enter the discount of the item(20% or higher): "))

final_price = calculate_discount(OrigignalPrice, discount_percent)

print(f"Final price after applying the discount: {final_price}")






















