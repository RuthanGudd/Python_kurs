from bankaccount import BankAccount

account = BankAccount(500)

amountToWithdraw = 300

result = account.try_withdraw(amountToWithdraw)

if (result.isSuccess):
    print(result.message)
