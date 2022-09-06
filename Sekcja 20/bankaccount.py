from result import Ok, Error


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def __str__(self):
        return str(self.balance)

    def deposit(self, amount=0):
        """Coś co sprawdza autentyczność/legalność pieniędzy"""
        self.balance += amount

    def try_withdraw(self, amount=0):
        if (self.balance >= amount):
            self.balance -= amount
            return Ok("Udało się", amount)

        return Error("Nie udało się", amount)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def try_withdraw(self, amount=0):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Error("Nie udało się, próba przekroczenia progu", amount)
