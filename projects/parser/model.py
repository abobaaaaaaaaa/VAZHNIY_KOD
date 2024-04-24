from bs4 import BeautifulSoup
import requests
import pandas as pd


class Parser:
    def __init__(self, page, container, class_container):
        self.page = page
        self.container = container
        self.class_container = class_container
        self.session = requests.Session()

    def request_answer(self):
        try:
            response = self.session.get(self.page)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            return str(e)

    def parser(self):
        try:
            response = self.session.get(self.page)
            response.raise_for_status()
            bs = BeautifulSoup(response.text, 'html.parser')
            result = bs.find_all(self.class_container, self.container)
            for i in range(len(result)):
                return result[i].text if result else None
        except requests.exceptions.RequestException as e:
            return str(e)
    def random_jokes(self):
        jokes=[]
        for k in range(10):
            jokes.append(self.parser())
        df=pd.DataFrame({'jokes':jokes})
        df.to_csv('jokes.csv')
