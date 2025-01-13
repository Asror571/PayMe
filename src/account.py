from .card import Card

class Account:

    def __init__(self, username, password, phone):
        self.__username = username
        self.__password = password
        self.__phone = phone
        self.__cards: list[Card] = list()

    def  change_password(self, new_password):
        self.__password = new_password

    def  change_username(self, new_username):
        self.__username = new_username

    def  change_phone(self, new_phone):
        self.__phone = new_phone

    def get_username(self):
        return self.__username
    
    def get_phone(self):
        return self.__phone

    def add_card(self, card: Card):
        self.__cards.append(Card)

    def get_balans(self):
        return sum(map(lambda card: card.money, self.__cards))
    