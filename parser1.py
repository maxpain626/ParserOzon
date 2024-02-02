import requests


def main():
    url = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2FsearchSuggestions%2F%3Ftext%3D%26url%3D%2Fsearch%2F%3Ftext%3D%7Bvalue%7D%26from_global%3Dtrue"
    response = requests.get(url=url)
    print(response.json())


if __name__ == '__main__':
    main()
    