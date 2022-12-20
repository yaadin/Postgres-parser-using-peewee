import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


class Parser:
    __URL = 'http://kenesh.kg/ru/deputy/list/35'

    def __init__(self):
        self.data = []
        self.soup = lambda html: BeautifulSoup(html, 'lxml')
        for page in range(1, self.get_last_page()+1):
            html = self.get_html(params=f'page={page}')
            cards = self.get_cards_from_html(html)
            list_of_deputates = self.parse_data(cards)
            self.data.extend(list_of_deputates)
        

    def get_html(self, params='') -> str:
        return requests.get(
            url=self.__URL,
            params=params
        ).text

    def get_cards_from_html(self, html) -> ResultSet:
        return self.soup(html).find_all("div", class_='dep-item')
    @staticmethod
    def parse_data(cards: ResultSet) -> list:
        result = []
        card: Tag
        for card in cards:
            name = card.find('a',class_='name').text
            fraction = card.find("div",class_='info').text
            try:
                phone = card.find('a',class_='phone-call').find('span').text
            except:
                phone = None
            try:
                email = card.find('a',class_='mail').find('span').text
            except:
                email = None
            obj = {'name':name,
                   'fraction':fraction,
                   'phone':phone,
                   'email':email,
                   }
            result.append(obj)
        return result
    
    def get_last_page(self):
        html = self.get_html()
        items = self.soup(html).find_all("a",class_='item')
        return max(map(lambda item:int(item.text),items))
    
if __name__ == "__main__":
    parser = Parser()
    print(parser.data)