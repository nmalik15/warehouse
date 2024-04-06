# Initialize account balance and warehouse inventory
account_balance = 0
inventory = {}
operations = []

# Main program loop
while True:
    print("\n*** >>  WAREHOUSE ACCOUNTING << ***")
    print("\nPlease select the number for action:")
    print("\t1. Balance - Add or subtract amount from account")
    print("\t2. Sale - Record a sale")
    print("\t3. Purchase - Record a purchase")
    print("\t4. Account - Display account balance")
    print("\t5. List - Display warehouse inventory")
    print("\t6. Warehouse - Display product status in warehouse")
    print("\t7. Review - Review recorded operations")
    print("\t8. END - Terminate program")

    command = input("\nEnter choice: ")

    if command == "1":
        print("\nDo you want to: ")
        print("\t1. Add to account balance ")
        print("\t2. Subtract from account balance ")
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = float(input("PLease enter amount to add to account balance: "))
            account_balance += amount
            operations.append(("Balance", amount))
            print(f"\nNEW ACCOUNT BALANCE: {account_balance}")

        elif choice == "2":
            amount = float(input("Plesae enter am ount to subtract from account balance: "))
            account_balance -= amount
            operations.append(("Balance", amount))
            print(f"\nNEW ACCOUNT BALANCE: {account_balance}")

        else:
            print("\n ERROR! INVALID COMMAND. TRY AGAIN.")
            
    elif command == "2":
        product = input("Enter product name: ")
        if product in inventory:
            price = inventory[product][1]
            quantity = int(input("Enter product quantity: "))
            if quantity <= inventory[product][0]:
                total_sale = price * quantity
                account_balance += total_sale
                inventory[product] = (inventory[product][0] - quantity, price)
                if inventory[product][0] == 0:
                    del inventory[product]
                operations.append(("Sale", (product, quantity, price, total_sale)))
                print(f"Sale recorded. New account balance: {account_balance}")
            else:
                print(f"Insufficient quantity of {product} in the inventory.")
        else:
            print(f"{product} is not available in the inventory.")

    elif command == "3":
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        total_cost = price * quantity
        if total_cost <= account_balance:
            account_balance -= total_cost
            if product in inventory:
                inventory[product] = (inventory[product][0] + quantity, price)
            else:
                inventory[product] = (quantity, price)
            operations.append(("Purchase", (product, quantity, price, total_cost)))
            print(f"Purchase recorded. New account balance: {account_balance}")
        else:
            print("ERROR! INSUFFICIENT BALNACE FOR THIS PURCHASE!")

    elif command == "4":
        print(f"\nCurrent account balance: {account_balance}")

    elif command == "5":


    elif command == "6":


    elif command == "7":


    elif command == "8":
        print("Terminating program...")
        break

    else:
        print("\n ERROR! INVALID COMMAND! PLEASE TRY AGAIN!")