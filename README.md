# Payme

classes:
- Account
    - properties:
        - username :private
        - password :private
        - phone : private
        - card :private
    - methods:
        - get_balans
        - change_password
        - change_username
- Card:
    - properties:
        - number
        - bank
        - expary_date
        - holder
    - methods:
        - deposite
        - withdraw

- Transaction
    - properties:
        - sender
        - reciever
        - money
        - date
    - method:
        - payment

- Currency:
    - properties:
        - url
    - method:
        - get_kurs
