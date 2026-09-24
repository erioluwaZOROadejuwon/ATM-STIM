
# ATM Simulator

A command-line ATM simulator built in Python — supports PIN authentication, checking balance, deposits, withdrawals, and transaction history, with proper error handling throughout.

## Features
- **PIN authentication** — user must enter the correct PIN before accessing the menu, with unlimited retries on incorrect attempts
- **Menu-driven interface**:
  1. Check Balance
  2. Deposit
  3. Withdraw
  4. Transaction History
  5. Exit
- **Deposit/Withdraw** handled through dedicated functions, using `raise` to reject invalid amounts (negative/zero) and insufficient funds on withdrawal
- **Transaction history** — every successful deposit/withdrawal is logged and viewable at any time
- **Input validation** — non-numeric input is caught with `try`/`except` instead of crashing the program

## How to run
```
python atm_simulator.py
```

Then:
1. Enter the correct PIN to unlock the menu
2. Choose an option (1–5) and follow the prompts
3. Choose Exit to end the session

## What I learned
- Structuring a program around small, focused functions (`check_balance()`, `deposit()`, `withdraw()`, `show_history()`) instead of one long script
- Using `global` to modify a variable defined outside a function — necessary since `balance` needs to persist and update across multiple function calls
- Using `raise` to enforce business rules (no negative amounts, no overdrafts) and `try`/`except` to catch and respond to those errors without crashing
- Using a list with `.append()` to build a transaction history, and looping through it with `for transaction in transaction_history` to display it
- The difference between `return` and `print()` — functions return values so the calling code decides what to do with them, rather than printing directly inside the function
- Knowing when `continue` actually matters (skipping code after it, still inside a loop) versus when it's harmless but unnecessary

## Tech
Python 3, no external dependencies

## Possible improvements
- Limit PIN attempts before locking the user out
- Save transaction history to a file so it persists between runs
- Support multiple accounts, each with their own PIN and balance



# 💰 Expense Tracker — Loan Calculator

A simple Python-based finance calculator that helps users calculate and understand the cost of a loan.

The project takes a user's **principal amount, annual interest rate, and loan term** and calculates the monthly repayment, total amount to be paid, total interest, and interest percentage. It also classifies the loan based on the interest charged.

## 🚀 Features

* 💵 Enter a loan/principal amount
* 📈 Enter an annual interest rate
* 📅 Enter the loan term in years
* 🧮 Calculate monthly loan repayment
* 💰 Calculate total amount to be paid
* 📊 Calculate total interest
* 📉 Calculate interest as a percentage of the total repayment
* 🏷️ Classify the loan as:

  * Low Interest
  * Moderate Interest
  * High Interest
* ⚠️ Handle invalid input using Python's `try/except`
* 🔢 Format financial values to two decimal places

## 🛠️ Technologies Used

* **Python 3**
* Functions
* Lambda functions
* Conditional statements
* Exception handling
* Mathematical operations
* f-strings
* User input

## 📂 Project Structure

```text
ATM-STIM/
│
├── fin.py
└── README.md
```

## ⚙️ How It Works

The program asks the user for three values:

```text
Principal Amount
Annual Interest Rate
Loan Term
```

It then uses the standard amortized loan repayment formula to calculate the monthly repayment:

```text
M = P × [r(1+r)ⁿ] / [(1+r)ⁿ - 1]
```

Where:

* `M` = Monthly repayment
* `P` = Principal amount
* `r` = Monthly interest rate
* `n` = Number of monthly payments

The annual interest rate is converted into a monthly decimal rate before being used in the calculation.

## ▶️ How to Run

### 1. Make sure Python is installed

Check your Python version:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone <your-repository-url>
```

### 3. Open the project folder

```bash
cd ATM-STIM
```

### 4. Run the program

```bash
python fin.py
```

## 💻 Example

```text
Track your loans and investments with our EXPENSE TRACKER

----------------------------------------
YOUR FINANCE SUMMARY
----------------------------------------

Enter your principal amount: 2000000
Enter your Annual Interest Rate: 20
Enter the term of your loan: 2

Monthly Repayment: ₦101,796.64
Total Amount: ₦2,443,119.36
Total Interest: ₦443,119.36
Percentage: 18.14%

Your loan is classified as: High Interest
```

*Example values are for demonstration purposes.*

## 🧠 What I Learned

This project helped me practice several important Python concepts:

* Creating and calling functions
* Passing arguments between functions
* Returning values from functions
* Using `global` variables
* Using lambda functions
* Handling errors with `try/except`
* Working with mathematical formulas
* Formatting numbers and currency
* Debugging Python errors
* Building a complete program from smaller functions

## 🔮 Future Improvements

Possible improvements for future versions include:

* [ ] Add a graphical user interface (GUI)
* [ ] Add investment calculations
* [ ] Add savings calculations
* [ ] Save loan records to a file
* [ ] Add transaction history
* [ ] Add a menu system
* [ ] Add data visualization
* [ ] Store user records using a database
* [ ] Add currency selection
* [ ] Improve input validation
* [ ] Build a web version

## 👨‍💻 About the Project

This project was created as part of my journey learning Python and building practical software projects.

It started as a simple calculator and is intended to grow into a more complete personal finance application.

---

⭐ **If you find this project useful, feel free to star the repository!**
