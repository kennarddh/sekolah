import requests



class Api:
    def __init__(self):
        self.baseUrl = 'http://localhost:4000'

    def name(self):
        return requests.get(f'{self.baseUrl}/name').json()
