# Inventory Management Tracker for Solar Car
# Tracks part names, categories, quantities, costs, and reorder levels.

inventory = [
    {"part": "Solar Panel", "category": "Electrical", "quantity": 8, "cost": 250.00, "reorder_level": 3},
    {"part": "Battery Module", "category": "Electrical", "quantity": 4, "cost": 450.00, "reorder_level": 2},
    {"part": "Carbon Fiber Panel", "category": "Body", "quantity": 6, "cost": 175.00, "reorder_level": 3},
    {"part": "Wheel Bearing", "category": "Mechanical", "quantity": 2, "cost": 45.00, "reorder_level": 4},
    {"part": "Brake Pad Set", "category": "Mechanical", "quantity": 5, "cost": 60.00, "reorder_level": 2}
]


def display_inventory():
    print("\n----- Solar Car Inventory -----")
    print(f"{'Part':<22}{'Category':<15}{'Qty':<8}{'Cost':<12}{'Reorder Level':<15}")
    print("-" * 72)

    for item in inventory:
        print(
            f"{item['part']:<22}"
            f"{item['category']:<15}"
            f"{item['quantity']:<8}"
            f"${item['cost']:<11.2f}"
            f"{item['reorder_level']:<15}"
        )


def show_low_stock():
    print("\n----- Low Stock Components -----")
    low_stock_found = False

    for item in inventory:
        if item["quantity"] <= item["reorder_level"]:
            print(
                f"{item['part']} | "
                f"Quantity: {item['quantity']} | "
                f"Reorder Level: {item['reorder_level']}"
            )
            low_stock_found = True

    if not low_stock_found:
        print("No components are currently low in stock.")


def calculate_inventory_value():
    total_value = 0

    for item in inventory:
        total_value += item["quantity"] * item["cost"]

    return total_value


def add_component():
    print("\n----- Add New Component -----")

    part = input("Part name: ")
    category = input("Category: ")
    quantity = int(input("Quantity: "))
    cost = float(input("Cost per unit: $"))
    reorder_level = int(input("Reorder level: "))

    new_item = {
        "part": part,
        "category": category,
        "quantity": quantity,
        "cost": cost,
        "reorder_level": reorder_level
    }

    inventory.append(new_item)
    print(f"{part} was added successfully.")


def update_quantity():
    print("\n----- Update Component Quantity -----")
    part_name = input("Enter the part name: ")

    for item in inventory:
        if item["part"].lower() == part_name.lower():
            new_quantity = int(input("Enter the new quantity: "))
            item["quantity"] = new_quantity
            print(f"{item['part']} quantity updated to {new_quantity}.")
            return

    print("Component not found.")


def main():
    while True:
        print("\n===== Solar Car Inventory Management Tracker =====")
        print("1. View Inventory")
        print("2. View Low Stock Components")
        print("3. View Total Inventory Value")
        print("4. Add Component")
        print("5. Update Component Quantity")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            display_inventory()

        elif choice == "2":
            show_low_stock()

        elif choice == "3":
            total_value = calculate_inventory_value()
            print(f"\nTotal Inventory Value: ${total_value:,.2f}")

        elif choice == "4":
            add_component()

        elif choice == "5":
            update_quantity()

        elif choice == "6":
            print("Exiting Inventory Management Tracker.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
