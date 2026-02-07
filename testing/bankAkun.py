import unittest

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20)
    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)
    def test_withdraw_zero(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)
    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
    def tearDown(self):
        self.account = None
        
if __name__ == '__main__':
    unittest.main()