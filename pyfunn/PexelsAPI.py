import requests
import random
from utils import *


class PexelsAPI:
    def __init__(self, API_KEY):
        self.API_KEY = str(API_KEY)
        self.headers = {'Authorization': API_KEY}
        self.path = 'https://api.pexels.com/'

    def GetPicsByQuery(self, query, per_page, page):
        params = {'query': query, 'per_page': str(per_page), 'page': str(page)}
        url = self.path + 'v1/search'

        response = (requests.get(url=url, params=params,
                                 headers=self.headers)).json()
        images = JsonToImageList(response)  # To be implemented
        return images

    def GetPicsByCurated(self, per_page, page):
        params = {'per_page': str(per_page), 'page': str(page)}
        url = self.path + 'v1/curated'

        response = (requests.get(url=url, params=params,
                                 headers=self.headers)).json()
        images = JsonToImageList(response)
        return images

    def GetPicByRandom(self):
        params = {'per_page': '1', 'page': str(random.randrange(1, 1000, 3))}
        url = self.path + 'v1/curated'

        response = (requests.get(url=url, params=params,
                                 headers=self.headers)).json()
        images = JsonToImageList(response)
        return images

    # Functions for video apis to be implemented.

    # https://www.pexels.com/api/documentation/
