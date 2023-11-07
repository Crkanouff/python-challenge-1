# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize an empty list to store customer orders
customer_order = []

# Welcome message
print("\nWelcome to the FOCO Food Truck.")

# Continuous ordering loop
while True:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    i = 1
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("\nType the menu number (or 'q'uit to finish ordering): ")

    if menu_category.lower() == 'q':
        break

    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]

        print(f"\nYou selected {menu_category_name}")

        i = 1
        menu_items = {}
        print()

        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(f"{key} - {key2}")
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {
                        "Item name": f"{key} - {key2}",
                        "Price": value2
                    }
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1

        menu_selection = input(f"Please enter the number for the {menu_category_name} item you would like to order: ")

        if menu_selection.isdigit() and int(menu_selection) in menu_items.keys():
            menu_selection = menu_items[int(menu_selection)]
            food_item = menu_selection["Item name"]
            item_price = float(menu_selection["Price"])

            quantity = input("How many would you like to order? (Default is 1): ")
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
            else:
                quantity = 1

            customer_order.append({"Item Name": food_item, "Price": item_price, "Quantity": quantity})
        else:
            print("\nInvalid menu item selection. Please try again.")
    else:
        print("\nInvalid menu category selection. Please try again.")

#6 Loop throu the items in the customer's order
print("\nGreat choices! This is what we are preparing for you:\n")

#7 Store the dictionary items as variables
for item in customer_order:
    item_name = item["Item Name"]
    item_price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    item_name_spaces = 30 - len(item_name)
    price_spaces = 10 - len(str(item_price))
    quantity_spaces = 10 - len(str(quantity))

    # 9. Create space strings
    item_name_space_str = " " * item_name_spaces
    price_space_str = " " * price_spaces
    quantity_space_str = " " * quantity_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_name_space_str} ${item_price}{price_space_str} {quantity}{quantity_space_str}")

# Thank the customer for their order
print("\nThank you for your order with the FOCO Food Truck!")

# Calculate the cost of the order using list comprehension
order_prices = [item["Price"] * item["Quantity"] for item in customer_order]

# Print the order list with titles and correct spacing
print("\nYour Order:")
print("{:<25} {:<10} {:<10} {:<10}".format("Item Name", "Price", "Quantity", "Total"))
print("-" * 55)

for item in customer_order:
    item_name = item["Item Name"]
    item_price = item["Price"]
    quantity = item["Quantity"]
    total = item_price * quantity

    # Create space strings using string multiplication
    item_name_space_str = " " * (25 - len(item_name))
    price_space_str = " " * (10 - len(str(item_price)))
    quantity_space_str = " " * (10 - len(str(quantity)))

    # Print each item with proper formatting using space strings
    print(f"{item_name}{item_name_space_str} ${item_price}{price_space_str} {quantity}{quantity_space_str}| ${total:.2f}")

# Calculate and print the total cost of the order
total_cost = sum(order_prices)
print("-" * 55)
print()
print(f"{'Total Cost:':<38} ${total_cost:.2f}")
print()
