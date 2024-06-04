import json
import requests


class OuterApiService:
    @staticmethod
    def random_dog_image():
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        return json.loads(response.content.decode()) if response.status_code == 200 else None

    @staticmethod
    def random_activity():
        response = requests.get("https://www.boredapi.com/api/activity")
        return json.loads(response.content.decode()) if response.status_code == 200 else None
