balance = 5000   # starting balance

print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful!")
    print("Updated balance:", balance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance! Withdrawal failed.")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
