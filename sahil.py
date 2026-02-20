balance = 5000  
def check_balance():
    print("\nYour current balance is ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print("Deposit successful!")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid amount!")
    else:
        balance -= amount
        print("Please collect your cash.")

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using ATM!")
        break   
    else:
        print("Invalid choice! Try again.")