from pprint import pprint
import requests
from pprint import pprint
import time
import requests
from ya_disk import YandexDisk
import time
import progressbar
import os
path = os.path.join(os.getcwd(), 'test.json')
import json



# _______________Считывание токена для работы с API VK яндекс диска_____________
with open('vk_token.txt', 'r') as token_vk:
    token_vk = token_vk.read().strip()
with open('ya_token.txt', 'r') as token_ya:
    token_ya = token_ya.read().strip()

URL = 'https://api.vk.com/method/photos.get'
owner_id = input('Введите ID пользователя VK: ')
params = {
    'owner_id': owner_id,
    'album_id': 'profile',
    'extended': 1,
    'access_token': token_vk,
    'v': '5.131'
}

resp = requests.get(URL, params =params)
# # ___________________URL___________

# # ______________количество фото профиля_________________________
quntity_foto = (len((resp.json()['response']['items'])))
# print(quntity_foto)
# # _____________________________количество лайков_________________________
# pprint((resp.json()['response']['items'][0]['likes']['count']))
temp = []
log = []
for foto in range(quntity_foto):
    url = (resp.json()['response']['items'][foto])['sizes'][-1]['url']
    like = (resp.json()['response']['items'][foto]['likes']['count'])
    size = (resp.json()['response']['items'][0])['sizes'][-1]['type']
    temp.append({'url': url, 'like': like})
    log.append({'file name': like, 'size': size})


if __name__ == '__main__':
    ya = YandexDisk(token=token_ya)
    ya.upload_file_to_disk(temp)
    with open(path, 'w') as data:
        json.dump(log, data)


