from src.account import Account
from src.card import Card
from src.transaction import Transaction


def main():
    c1 = Card("Olik", 1234123412341234, 'SQB', 1_000_000)
    c2 = Card("Bissnes", 678967896789, 'NBU', 18_000_000)
    a1 = Account('ali', 123, "998991231212")
    
    c3 = Card("Pensiya", 1234123412341234, 'SQB', 1_000_000)
    c4 = Card("Visa", 678967896789, 'Visa', 18_000_000)
    a2 = Account('vali', 123, "998991231212")

    t = Transaction(c2, c3, 120000)
    t.payment()
    t.get_check()
    
    print(c2.money)


if __name__ == '__main__':
    main()