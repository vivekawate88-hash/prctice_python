# def deposit(balance=0,amount=0):
#     return balance+amount

# def withdraw(balance,amount=0):
#     return balance-amount

# balance=deposit(0,100)

# print("Balance after Deposit:", balance)

# balance=withdraw(balance,90)
# print('Balance after withdraw:', balance)

bal = 0
def deposit(amt):
    global bal
    if amt>0:
        bal=bal + amt
        print("Depoist Successfully:")
        
    else:
        print('Enter vaild amount:')
        
    

def withdraw(amt):
    global bal
    if amt>bal:
        print("Insufficient balance",bal)
    elif amt==0 :
        print("pls enter valid amt") 
    else:
        print("withdraw Successfull",bal-amt)
        


a=int(input("Enter amount:"))
deposit(a)
b=int(input("Enter amount to withdraw:"))
withdraw(b)





