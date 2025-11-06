def withdraw(balance,amount):
    if amount > balance:
        raise ValueError("Sorry, Insufficient Amount!")
    else:
        balance -=amount
        print("Withdraw successful. Reminding Balance is : ",balance)


try:
    balance = 1000
    print("Your current balance is : ",balance)
    amount = float(input("Enter the amount to withdraw: "))
    withdraw(balance,amount)

except ValueError as e:
    print("Transaction error",e)

except Exception:
    print("Sorry, something went wrong and please try again.")
    

finally:
    print("Transaction completed.")