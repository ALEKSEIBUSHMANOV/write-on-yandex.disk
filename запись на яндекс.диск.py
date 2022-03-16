import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        url = response.json()["href"]
        response = requests.put(url, data=open(path_to_file, 'rb'))


if __name__ == '__main__':
    path_to_file = ....
    token = ....
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)