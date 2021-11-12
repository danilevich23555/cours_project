from ya_disk import YandexDisk
from settings import tokens
from VK_URL import get_VK_URL
import os
path = os.path.join(os.getcwd(), 'test.json')
import json



# # _______________Считывание токена для работы с API VK яндекс диска_____________
# # with open('vk_token.txt', 'r') as token_vk:
# #     token_vk = token_vk.read().strip()
# # with open('ya_token.txt', 'r') as token_ya:
# #     token_ya = token_ya.read().strip()
# #
# # URL = 'https://api.vk.com/method/photos.get'
# # owner_id = input('Введите ID пользователя VK: ')
# # params = {
# #     'owner_id': owner_id,
# #     'album_id': 'profile',
# #     'extended': 1,
# #     'access_token': token_vk,
# #     'v': '5.131'
# # }
#
# resp = requests.get(URL, params =params)
# quntity_foto = (len((resp.json()['response']['items'])))
#
# temp = []
# log = []
# for foto in range(quntity_foto):
#     url = (resp.json()['response']['items'][foto])['sizes'][-1]['url']
#     like = (resp.json()['response']['items'][foto]['likes']['count'])
#     size = (resp.json()['response']['items'][0])['sizes'][-1]['type']
#     temp.append({'url': url, 'like': like})
#     log.append({'file name': like, 'size': size})


if __name__ == '__main__':
    ya = YandexDisk(token=tokens()[1])
    ya.upload_file_to_disk(get_VK_URL()[0])
    with open(path, 'w') as data:
        json.dump(get_VK_URL()[1], data)


