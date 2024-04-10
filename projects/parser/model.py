from bs4 import BeautifulSoup
import requests

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
            result = bs.find(self.class_container, self.container)
            return result.text if result else None
        except requests.exceptions.RequestException as e:
            return str(e)
