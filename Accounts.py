class Accounts:
    """ This class maintain account's details """

    FilePath = "./Bank_DataBase/UsersData.csv"
    Members = {}

    def __init__(self):
        if len(Accounts.Members) == 0:
            self.Account_Id = ""
            if len(Accounts.Members) == 0:
                self.LoadAccounts()

    def LoadAccounts(self):
        print("\n")
        Accounts.Members.clear()

        with open(Accounts.FilePath, "r") as F:
            Lines = F.readlines()

        for Line in Lines:

            if len(Line.strip()) > 0:
                SplitLines = Line.split(",")
                Account_Holder_Number = SplitLines[0].strip()
                Account_Holder_Name = SplitLines[1].strip()
                Account_Holder_Pin = SplitLines[2].strip()

                Accounts.Members[Account_Holder_Number] = {"Name": Account_Holder_Name, "Pin": Account_Holder_Pin}

        #print(Accounts.Members)

    def ValidateAccount(self, Account_Id):

        if Account_Id in Accounts.Members:
            self.Account_Id = Account_Id
            return Accounts.Members[Account_Id]["Name"]
        else:
            raise Exception("Invaild Account Number")

    def ValidatePin(self, Pin):

        if self.Account_Id in Accounts.Members:
            pinnumber = Accounts.Members[self.Account_Id]["Pin"]
            return Pin == pinnumber

        else:
            raise Exception("Invalid Pin")
