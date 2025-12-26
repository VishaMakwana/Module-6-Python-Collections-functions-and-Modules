
# FIXTRACK - Gadget Repair Tracking System

repair_orders = []   # temporary in-memory list to store all orders



# Function: Book a new order

def book_repair_order():
    print("\n--- Book a New Repair Order ---")

    name = input("Customer Name: ")
    device = input("Device Type: ")
    issue = input("Issue Description: ")
    due_date = input("Due Date: ")

    order = {
        "name": name,
        "device": device,
        "issue": issue,
        "due_date": due_date
    }

    repair_orders.append(order)
    print("\nOrder added successfully!")
    print(f"Total orders: {len(repair_orders)}")



# Function: Billing System

def generate_bill():
    print("\n--- Generate Bill ---")

    if not repair_orders:
        print("No orders available! Please add orders first.")
        return

    # Show order list
    print("\nAvailable Orders:")
    for i, order in enumerate(repair_orders, start=1):
        print(f"{i}. {order['name']} - {order['device']}")

    try:
        index = int(input("\nSelect order number: ")) - 1
        selected_order = repair_orders[index]
    except:
        print("Invalid selection!")
        return

    parts_cost = float(input("Enter parts cost: "))
    repair_fee = float(input("Enter repair fee: "))
    tax_rate = 0.10  

    subtotal = parts_cost + repair_fee
    tax_amount = subtotal * tax_rate

    discount = float(input("Enter discount (0 if none): "))

    final_total = subtotal + tax_amount - discount

    print("\n------ FIXTRACK INVOICE ------")
    print(f"Customer Name : {selected_order['name']}")
    print(f"Device        : {selected_order['device']}")
    print(f"Issue         : {selected_order['issue']}")
    print(f"Due Date      : {selected_order['due_date']}")
    print("----------------------------------")
    print(f"Parts Cost    : {parts_cost}")
    print(f"Repair Fee    : {repair_fee}")
    print(f"Subtotal      : {subtotal}")
    print(f"Tax (10%)     : {tax_amount}")
    print(f"Discount      : {discount}")
    print("----------------------------------")
    print(f"Final Total   : {final_total}")
    print("----------------------------------")

    print("\nBill generated successfully!")

# Main Menu

def main_menu():
    while True:
        print("\n===== FIXTRACK SYSTEM =====")
        print("1. Book Repair Order")
        print("2. Generate Bill")
        print("3. View All Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_repair_order()
        elif choice == "2":
            generate_bill()
        elif choice == "3":
            print("\n--- All Repair Orders ---")
            for o in repair_orders:
                print(o)
        elif choice == "4":
            print("Exiting FixTrack. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
main_menu()
