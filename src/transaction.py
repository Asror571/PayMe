from .card import Card


class Transaction:

    def __init__(self, sender: Card, reciever: Card, money: float):
        self.__sender: Card = sender
        self.__reciever: Card = reciever
        self.__money: float = money

    def payment(self):
        self.__sender.withdraw(self.__money)
        self.__reciever.deposite(self.__money)

    def get_check(self):
        print(f"""yuboruvchi: {self.__sender.number}\nqabul qiluvchi: {self.__reciever.number}\n\n\
            pul: {self.__money}""")