from pprint import pprint

import requests
import time
import progressbar

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }




    def upload_file_to_disk(self, dict_vk):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        quantity = len(dict_vk)
        for counter in range(quantity):
            for i in progressbar.progressbar(range(1)):
                url = dict_vk[counter]['url']
                disk_file_path = dict_vk[counter]['like']
                params = {"url": url, "path": disk_file_path}
                headers = self.get_headers()
                response = requests.post(upload_url, params=params, headers=headers)
        print(f'{int(quantity)} фото загружено на Яндекс диск')

