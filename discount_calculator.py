def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))

discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
