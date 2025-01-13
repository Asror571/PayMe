class Card:

    def __init__(self, holder, number, bank, money):
        self.holder = holder
        self.number = number
        self.bank = bank
        self.money = money

    def deposite(self, money):
        if money > 0:
            self.money += money

    def withdraw(self, money):
        if self.money > 0 and self.money >= money:
            self.money -= money

