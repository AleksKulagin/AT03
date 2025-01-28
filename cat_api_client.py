import requests


def get_random_cat_image(api_url="https://api.thecatapi.com/v1/images/search"):
    """
    Делает запрос к TheCatAPI и возвращает URL случайного изображения кошки.
    :param api_url: URL API сервиса
    :return: URL изображения кошки (str) или None в случае ошибки
    """
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0 and "url" in data[0]:
                return data[0]["url"]
        return None
    except requests.RequestException:
        return None