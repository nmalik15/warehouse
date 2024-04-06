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
        

    elif command == "3":


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