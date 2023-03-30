import requests

def busca_usuari (usuario):
    """
    buscar usuario no github por api
    :param usuario: enviar o str do usuario no github
    :return: str jison com os dados
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(busca_usuari('ponsoniro2023'))


