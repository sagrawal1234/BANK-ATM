class ATM(object):
  def __init__(self,cardNo,pinNo,custName):
    self.cardNo=cardNo
    self.pinNo=pinNo
    self.balance=0
    self.custName=custName
  def cashWithdraw(self,amount):
    if self.balance-amount > 0:
      self.balance=self.balance-amount
      print("Rs.",amount," withdrawn. Balance: Rs.",self.balance)
    else:
      print("Insufficient balance.")

  def cashDeposit(self,amount):
    self.balance=self.balance+amount
    print("Rs. ",amount," deposited. Balance: Rs.",self.balance)


  def balanceEnquiry(self):
    print("Balance in your account: Rs.",self.balance," only.")

#already accounts registered
cust1=ATM("1234 5678 9999","1234","raj")
cust2=ATM("1234 5678 2222","3456","simran")
cust3=ATM("1234 5678 5555","5678","rahul")


print("Welcome to ATM")
cardNo=input("Enter your card no:")
pinNo=input("Enter your pin no:")

#allow only registered users to use the ATM
if(cardNo==cust1.cardNo or cardNo==cust2.cardNo or cardNo==cust2.cardNo):
  if(cardNo==cust1.cardNo):
    flag="cust1"
  elif(cardNo==cust2.cardNo):
    flag="cust2"
  elif(cardNo==cust3.cardNo):
    flag="cust3"
  else:
    flag=""
  if(flag=="cust1" and pinNo==cust1.pinNo):
    check=True
    obj=cust1
    print("Welcome ",obj.custName)
  elif(flag=="cust2" and pinNo==cust2.pinNo):
    check=True
    obj=cust2
    print("Welcome ",obj.custName)
  elif(flag=="cust3" and pinNo==cust3.pinNo):
    check=True
    obj=cust3
    print("Welcome ",obj.custName)
  else:
      print("Incorrect pin.")
      check=False
  while(check):
    print("Menu:")
    print("1. Balance check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    ch=int(input("Enter your choice:"))
    
    if(ch==1):
      obj.balanceEnquiry()
    elif(ch==2):
      a=int(input("Enter the amount: Rs."))
      obj.cashDeposit(a)
    elif(ch==3):
      a=int(input("Enter the amount: Rs."))
      obj.cashWithdraw(a)
    else:
      print("Thank you.. visit again..")
      check=False
else:
  print("No such account found in records. Please contact branch to register.")