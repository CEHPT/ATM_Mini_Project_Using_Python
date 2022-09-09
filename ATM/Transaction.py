from datetime import datetime


class Transactions:
    """This class maitain withdraw , deposite , List transactions"""

    FilePath = "./Bank_DataBase/ListTransactions.csv"

    def __init__(self):
        self.ClosingBalance = 0

    def ListTransaction(self, Account_Id):

        self.ClosingBalance=0
        with open(Transactions.FilePath, "r") as F:
            Lines = F.readlines()

            Trans = []

            for Line in Lines:
                Fields = Line.split(",")

                # print(Fields[0],Account_Id)

                if Fields[0] == Account_Id:
                    Trans.append(Line.strip())

            # print(Trans)

        print("\n")
        print("List Transactions")
        print("=================")

        print("   Date      Time                  Transactions")
        print("   ----      ----                  ------------\n")
        for l in Trans:
            Fields = l.split(",")

            if Fields[0] == Account_Id:
                date_time = Fields[1]
                D_Or_W = Fields[2]
                ammount = float(Fields[3])

                if D_Or_W == "Withdraw":
                    ammount = -ammount

                self.ClosingBalance += ammount

            print("{} {:>20s} {:10.2f} ".format(date_time, D_Or_W, ammount))
        print("\nClosing Balance = %.2f" % self.ClosingBalance)

    def Deposit(self, AccountId, Amount):

        Current_Date = datetime.now().strftime("%d/%m/%Y %X")

        with open(Transactions.FilePath, "a") as F:
            F.write("{0},{1},Deposit,{2}\n".format(AccountId, Current_Date, Amount))

    def Withdraw(self, AccountId, Amount):

        Current_Date = datetime.now().strftime("%d/%m/%Y %X")

        with open(Transactions.FilePath, "a") as F:
            F.write("{0},{1},Withdraw,{2}\n".format(AccountId, Current_Date, Amount))
