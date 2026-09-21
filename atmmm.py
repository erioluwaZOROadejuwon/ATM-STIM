print("Welcome to our Banking Services.......")
pin= "0000"
while True:
    auth = input("Enter your pin: ").strip()
    if auth==pin:
        print("Correct Pin")
        break
    else:
        print("Invalid Pin, try again later....")
       

balance = 50000
trans_hist = []

def check_balance():
    return balance

def deposit(amount):
    if amount<=0:
        raise ValueError("Deposit an amount that exceeds 0 ")
    global balance
    balance+=amount
    trans_hist.append(f"Withdrew{amount}, your new balance:{balance}")
    return balance

def Withdraw(amount):
    global balance
    if amount>balance:
        raise ValueError(" Insufficient Funds.........Fund your Wallet")
    if amount <=0:
        raise ValueError(" Enter a Valid number")
    balance-=amount
    trans_hist.append(f"Withdrew{amount}, your new balance:{balance}")
    return balance

def Transactions():
    if not trans_hist:
        print("No transactions yet")
        return
    print("Transaction History.......")
    for transaction in trans_hist:
        print(transaction)



while True:
    modules=input("Enter 1- to check balance, 2- to deposit money, 3- to withdraw money, 4- to check your transaction history, 5- EXIT")
    if modules == "5":
        Warning=input("Are you sure you want to exit (y/n)")
        if Warning.lower() != "y":
            print("Thanks for banking with us")
            break
        else:
            print("......")
            continue
    elif modules=="1":
        print(f"Balance:{check_balance()}")
    elif modules=="2":
        try:
            amount = float(input("Enter the amount you want to deposit:"))
            deposit(amount)
            print(f"New balance......{check_balance()}")
        except ValueError as D:
            print(f"Invalid input{D}")
    elif modules=="3":
        try:
            amount = float(input("Enter the amount you want to withdraw:"))
            Withdraw(amount)
            print(f"Withdrawal Successful......Your balance is {check_balance()}")
        except ValueError as D:
            print(f"Error{D}")
    elif modules=="4":
        Transactions()
    else:
        print("Invalid option")
        continue
    
   
