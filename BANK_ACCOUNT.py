def Bank_Class():
    def __init__(self,acc_num,acc_type,acc_balance,acc_pin):
        self . Acc_Number = acc_num
        self . Acc_Type = acc_type
        self . Acc_Balance = acc_balance
        self . Acc_Pin = acc_pin
        self.Greeting()
    def Greeting(self):
        print("WELCOME TO OUR BANK YOUR BANK")
        account = int(input("ENTER THE ACCOUNT NUMBER"))
        pin = int(input("ENTER THE PIN TO CONTINUE"))
        if(pin == self.Acc_Pin):
            self.Functions()
        else:
            print("YOU ENTERED A WRONG PIN OR WRONG ACCOUNT NUMBER")
            exit()    
    def Functions(self):
        print(f''' WELCOME TO FUNCTION PANEL
                   YOUR ACCOUNT NUMBER {self.Acc_Number}
                   YOUR ACCOUNT TYPE {self.Acc_Type}
                    PRESS 1 TO CHANGE PIN
                    PRESS 2 TO CHECK BALANCE
                    PRESS 3 TO DEPOIST CASH
                    PRESS 4 TO WITDRAW CASH
                    ANY WRONG ENTRY WILL CLOSE PROGRAM
                    ''')
        choice = int(input("ENTER YOUR CHOICE TO CONTINUE FURTHER"))
        if (choice == 1 ):
            Change_Pin()
        elif(choice == 2):
            Balance_Check()
        elif(choice == 3):
            Deposit()
        elif(choice == 4):
            Witdraw()
        else:
            exit()
    def Change_Pin(self):
        pin = int(input("ENTER THE OLD PIN TO CONTINUE"))
        if(pin == self.Acc_Pin):
            new_pin = int(input("ENTER THE NEW PIN"))
            self.Acc_Pin = new_pin
            print("PIN HAS BEEN CHANGED SUCESSFULLY")
            Functions()
        else:
            print("YOU ENTERED A WRONG PIN ")
            exit()    
    def Balance_Check(self):
        pin = int(input("ENTER THE PIN TO CONTINUE"))
        if(pin == self.Acc_Pin):
            print(f"YOUR BALANCE IS {self.Acc_Balance}")
            Functions()
        else:
            print("YOU ENTERED A WRONG PIN ")
            exit()
    def Deposit(self):
        pin = int(input("ENTER THE PIN TO CONTINUE"))
        if(pin == self.Acc_Pin):
            money = int(input("ENTER THE MONEY"))
            self.Acc_Balance = self.Acc_Balance + money
            print(f"DEPOSIT COMPLETE YOUR BALANCE IS {self.Acc_Balance}")
            Functions()
        else:
            print("YOU ENTERED A WRONG PIN ")
            exit()
    def Witdraw(self):
        pin = int(input("ENTER THE PIN TO CONTINUE"))
        if(pin == self.Acc_Pin):
            money = int(input("ENTER THE MONEY YOU WANT TO WIDRAW"))
            if(self.Acc_Type == "PERSONAL"):
                bank_fee = (money/100)*5
                bank_limit = 25000
            if(self.Acc_Type == "BUSINESS"):
                bank_fee = (money/100)*2
                bank_limit = 200000
            if(money>bank_limit):
                print("LIMIT EXCEEDED")
                Functions()
            else:
                self.Acc_Balance = (self.Acc_Balance - (money + bank_fee))
                print(f"WIDRAW COMPLETE YOUR BALANCE IS {self.Acc_Balance} AND BANK FEE WAS {bank_fee}")
                Functions()
        else:
            print("YOU ENTERED A WRONG PIN ")
            exit()
account_1 = Bank_Class(1,"PERSONAL",100000,1234) 
