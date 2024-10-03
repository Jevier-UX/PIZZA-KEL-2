print("=== Welcome to Noirr Pizza ===")
print("Please place order here")

pizza_menu = {
    "Frankfurter BBQ": 35.000,
    "Meat Monsta": 35.000,
    "Super Supreme": 40.000,
    "Super Supreme Chicken": 50.000,
    "Meat Lover": 60.000, 
    "Chicken Lover": 50.000,
    "Cheese Lover": 40.000,
    "American Favorite": 50.000,
}

crust_menu = {
    "Pan Crust": 0,
    "Thick Crust": 5.000,
    "Cheese Burst": 10.000,
}

toppings_menu = {
    "Extra Cheese": 13.000,
    "Mushrooms": 8.000,
    "Pepperoni": 8.000,
}

size_menu = {
    "Small": 0,
    "Medium": 5.000,
    "Large": 15.000,
}

def print_menu(menu):
    for item, price in menu.items():
        print(f"{item}: Rp{price:.3f}")

def choose_item(menu, item_type):
    while True:
        choice = input(f"Please choose your {item_type} (type 'none' to skip): ").title()
        if choice == 'None':
            return None, 0
        elif choice in menu:
            print(f"{choice} selected. Price: Rp{menu[choice]:.3f}")
            return choice, menu[choice]
        else:
            print("Invalid choice. Please choose from the menu.")

def order_pizza():
    print("\n=== Pizza Menu ===")
    print_menu(pizza_menu)
    pizza, price = choose_item(pizza_menu, "pizza")
    if pizza:
        size, size_price = choose_size()
        return pizza, price + size_price, size
    else:
        return None, 0, None

def order_crust():
    print("\n=== Crust Menu ===")
    print_menu(crust_menu)
    crust, price = choose_item(crust_menu, "crust")
    if crust:
        return crust, price
    else:
        return None, 0

def order_toppings():
    print("\n=== Toppings Menu ===")
    print_menu(toppings_menu)
    total_toppings_cost = 0
    while True:
        topping, price = choose_item(toppings_menu, "topping")
        if topping:
            total_toppings_cost += price
        else:
            break
        more_toppings = input("Do you want to add more toppings? (yes/no): ").lower()
        if more_toppings != "yes":
            break
    return total_toppings_cost

def choose_size():
    print("\n=== Size Menu ===")
    print_menu(size_menu)
    size, price = choose_item(size_menu, "size")
    if size:
        return size, price
    else:
        return "Medium", 5.000  

def display_final_bill(pizza, size, crust, total_cost, toppings_cost):
    print("\n=== Summary Of Your Order ===")
    print(f"Pizza: {pizza if pizza else 'No pizza selected'}")
    print(f"Size: {size if size else 'No size selected'}")
    print(f"Crust: {crust if crust else 'No crust selected'}")
    print(f"Toppings: Rp{toppings_cost:.3f}")
    final_total = total_cost + toppings_cost
    print(f"Total: Rp{final_total:.3f}")

total_cost = 0

if __name__ == "__main__":
    pizza, pizza_cost, size = order_pizza()
    total_cost += pizza_cost
    
    if pizza:
        crust, crust_cost = order_crust()
        total_cost += crust_cost
        toppings_cost = order_toppings()
        display_final_bill(pizza, size, crust, total_cost, toppings_cost)
    else:
        print("You must select a pizza to complete the order.")