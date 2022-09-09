from ATM import Accounts
from ATM import Transaction


class ATM_Menu:
    ac = Accounts.Accounts()
    txt = Transaction.Transactions()

    def __init__(self):
        self.Account_number = ""

    @classmethod
    def Start(self):

        while True:

            print("Kanchipuram Bank Pvt Ltd..")
            print("--------------------------")

            # verify account number
            account_number = input("Enter The Account Number : ")

            try:
                Account_Name = ATM_Menu.ac.ValidateAccount(account_number)
                self.Account_number = account_number
                print("Welcome %s" % Account_Name)

            except Exception as e:
                print("Invalid Account Number Press Enter To Continue.....")
                input()
                continue

            # verify pin
            pinnumber = input("Enter The PIN Number : ")

            if not ATM_Menu.ac.ValidatePin(pinnumber):
                print("Invalid Pin Press Enter To Continue....")
                input()
                continue

            self.TransactionMenu()

    @classmethod
    def TransactionMenu(self):

        print("Choice Your Option\n")

        while True:

            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.List Transactions")
            print("4.Exit")

            choice = int(input("\nEnter The Choice (1-4) : "))

            if choice == 4:
                break

            elif choice == 1:
                money = float(input("\nEnter  Amount To Deposit : "))
                ATM_Menu.txt.Deposit(self.Account_number, money)
                print("Deposit Successfully .Press Enter To Continue")
                input()
                continue

            elif choice == 2:
                money = float(input("\nEnter  Amount To Withdraw : "))
                if self.txt.ClosingBalance >= money > 0:
                    ATM_Menu.txt.Withdraw(self.Account_number, money)
                    print("Withdraw Successfully .Press Enter To Continue")
                    input()
                    continue
                else:
                    print("Insufficient Balance! .Press Enter To Continue ")
                    input()
                    continue

            elif choice == 3:
                ATM_Menu.txt.ListTransaction(self.Account_number)
                print("Press Enter To Continue")
                input()
                continue

            else:
                print("Invalid Option .Press Enter To Continue")
                input()
