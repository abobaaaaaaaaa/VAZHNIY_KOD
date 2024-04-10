from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, page, container, class_container):
        self.page = page
        self.container = container
        self.class_container = class_container

    def request_answer(self):
        url = requests.get(self.page)
        if url.status_code == 200:
            return True
        else:
            return url.status_code

    def parser(self):
        bs = BeautifulSoup(requests.get(self.page).text)
        return bs.find(self.class_container, self.container)