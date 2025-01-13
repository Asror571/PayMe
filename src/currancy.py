import requests

class Currancy:
    __url = "https://nbu.uz/uz/exchange-rates/json/"

    def calculate(self, money, code):
        for i in self.get_state():
            if i['code'] == code:
                return round(money / float(i['nbu_buy_price']), 2)

    def get_state(self):
        r = requests.get(self.__url)
        data = r.json()
        return data
        