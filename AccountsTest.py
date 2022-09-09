from ATM import Accounts
from ATM import Transaction
from ATM import Menu

o = Accounts.Accounts()
o.LoadAccounts()

try:
    Account_Holder_Name = o.ValidateAccount("2")
    print("Vaild Account Number.\nAccount Name : ", Account_Holder_Name)

    if o.ValidatePin("2222"):
        print("Vaild Pin.")

        obj = Transaction.Transactions()
        #obj.Deposit(o.Account_Id, 10560)
        obj.ListTransaction("2")

        del obj

    else:
        print("Invalid Pin.")

except Exception as e:
    print("Error : " + str(e))

del o
