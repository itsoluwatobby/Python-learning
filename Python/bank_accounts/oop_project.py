from bank_account import *

Dave = BankAccount(10_000, 'Dave')
Mark = BankAccount(2100, 'Mark')

Dave.getBalance()
Mark.getBalance()

Dave.deposit(5000)
Dave.withdraw(1_000)
Dave.transfer(10_000, Mark)

Sam = InterestRewardsAccount(1000, 'Sam')

Sam.getBalance()
Sam.deposit(100)
Sam.transfer(1000, Dave)

Blaze = SavingAccount(1000, 'Blaze')

Blaze.getBalance()
Blaze.deposit(200)

Blaze.transfer(500, Mark)
