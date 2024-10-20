menu = {
    'Pizza':50,
    'Pasta':80,
    'Burger':30,
    'Sandwich':40,
    'Green Salad': 20,
    'Fries':30,
    'Soda':20,
    'Water':20,
    'Ice Cream':50,
}

print("Welcome to PYTHON RESTAURANT")
print("Pizza : Rs 50\nPasta: Rs 80\nBurger: Rs 30\nSandwich : Rs 40\ngreen Salad: Rs 20\nFries: Rs 30\nSoda : Rs 20\nWater: Rs 20\nIce Cream: Rs 50")

order_total = 0

item_1 = input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item {} has been added to your order".format(item_1))
else:
    print("Sorry, we don't have {} in our menu yet!".format(item_1))
   
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" :
    item_2 = input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Your item {} has been added to your order".format(item_2))
    else:
        print("Sorry, we don't have {} in our menu!".format(item_2))
print("The Total Amount Of Items To Pay Is {}".format(order_total))      