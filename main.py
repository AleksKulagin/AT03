import pytest
import requests
import requests_mock
from cat_api_client import get_random_cat_image


def test_successful_cat_image_request():
    """
    Тестирует успешный запрос к API, возвращающий корректный URL изображения кошки.
    """
    with requests_mock.Mocker() as mock:
        mock.get(
            "https://api.thecatapi.com/v1/images/search",
            json=[{"url": "https://cdn2.thecatapi.com/images/cat.jpg"}],
            status_code=200,
        )
        result = get_random_cat_image()
        assert result == "https://cdn2.thecatapi.com/images/cat.jpg"


def test_unsuccessful_request_404():
    """
    Тестирует случай, когда сервер возвращает 404 статус (not found).
    """
    with requests_mock.Mocker() as mock:
        mock.get("https://api.thecatapi.com/v1/images/search", status_code=404)
        result = get_random_cat_image()
        assert result is None


def test_no_url_key_in_response():
    """
    Тестирует случай, когда API возвращает данные без ключа 'url'.
    """
    with requests_mock.Mocker() as mock:
        mock.get(
            "https://api.thecatapi.com/v1/images/search",
            json=[{"id": "abc123"}],
            status_code=200,
        )
        result = get_random_cat_image()
        assert result is None


def test_exception_handling():
    """
    Тестирует обработку ситуации, когда запрос вызывает исключение (например, сеть недоступна).
    """
    with requests_mock.Mocker() as mock:
        mock.get("https://api.thecatapi.com/v1/images/search", exc=requests.ConnectionError)
        result = get_random_cat_image()
        assert result is None

if __name__ == "__main__":
    pytest.run(main())