from bankaccount import BankAccount

account = BankAccount()
print(account)

account.deposit(500)
print(account)

account.withdraw()
print(account)

account.withdraw(300)
print(account)
