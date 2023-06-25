import tkinter as tk


class Account:
    def __init__(self, account_number, account_type):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.account_type == "savings" and self.balance - amount < 0:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}")


class BankAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank App")

        # Set color for GUI elements
        self.background_color = "pink"
        self.button_color = "pink"
        self.label_color = "black"
        self.entry_color = "white"

        # Set GUI layout
        self.root.configure(bg=self.background_color)

        # Create the Bank instance
        self.bank = Bank()

        # Create labels
        self.label_account_number = tk.Label(root, text="Account Number:", bg=self.background_color, fg=self.label_color)
        self.label_account_type = tk.Label(root, text="Account Type:", bg=self.background_color, fg=self.label_color)
        self.label_amount = tk.Label(root, text="Amount:", bg=self.background_color, fg=self.label_color)

        # Create entry fields
        self.entry_account_number = tk.Entry(root, bg=self.entry_color)
        self.entry_account_type = tk.Entry(root, bg=self.entry_color)
        self.entry_amount = tk.Entry(root, bg=self.entry_color)

        # Create buttons
        self.button_create_account = tk.Button(root, text="Create Account", bg=self.button_color, command=self.create_account)
        self.button_deposit = tk.Button(root, text="Deposit", bg=self.button_color, command=self.deposit)
        self.button_withdraw = tk.Button(root, text="Withdraw", bg=self.button_color, command=self.withdraw)

        # Set GUI grid layout
        self.label_account_number.grid(row=0, column=0, padx=10, pady=10)
        self.label_account_type.grid(row=1, column=0, padx=10, pady=10)
        self.label_amount.grid(row=2, column=0, padx=10, pady=10)
        self.entry_account_number.grid(row=0, column=1, padx=10, pady=10)
        self.entry_account_type.grid(row=1, column=1, padx=10, pady=10)
        self.entry_amount.grid(row=2, column=1, padx=10, pady=10)
        self.button_create_account.grid(row=3, columnspan=2, padx=10, pady=10)
        self.button_deposit.grid(row=4, columnspan=2, padx=10, pady=10)
        self.button_withdraw.grid(row=5, columnspan=2, padx=10, pady=10)

    def create_account(self):
        account_number = self.entry_account_number.get()
        account_type = self.entry_account_type.get()

        if account_number and account_type:
            self.bank.create_account(account_number, account_type)
            print("Account created successfully.")
        else:
            print("Please enter account number and type.")

    def deposit(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())

        if account_number and amount:
            self.bank.deposit(account_number, amount)
            print("Deposit successful.")
        else:
            print("Please enter account number and amount.")

    def withdraw(self):
        account_number = self.entry_account_number.get()
        amount = float(self.entry_amount.get())

        if account_number and amount:
            self.bank.withdraw(account_number, amount)
            print("Withdrawal successful.")
        else:
            print("Please enter account number and amount.")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type):
        account = Account(account_number, account_type)
        self.accounts.append(account)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


# Create the Tkinter root window
root = tk.Tk()

# Initialize the BankAppGUI
app = BankAppGUI(root)

# Start the GUI event loop
root.mainloop()
