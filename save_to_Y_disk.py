import os
import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        API_YANDEX = "https://cloud-api.yandex.net/"
        token = "AQAAAABJla86AADLWxD3cBm2aE9KuTY4sWN-Rg8"
        file_list = os.listdir(file_path)
        headers = {
            "accept": "application/json",
            "authorization": f"OAuth {token}"
        }

        for file_name in file_list:
            file_dir = "hw/" + file_name.lower()
            r = requests.get(API_YANDEX + "v1/disk/resources/upload", params={"path": file_dir}, headers=headers)
            path_to_file = file_path + file_name
            requests.put(r.json()["href"], headers=headers, files={"file": open(path_to_file, "rb")})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:/Users/VedNA/Pictures/hw/"
    token = "AQAAAABJla86AADLWxD3cBm2aE9KuTY4sWN-Rg8"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)






