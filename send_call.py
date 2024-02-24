import os
import requests


def verify_token(token):
    response = requests.post('http://example.com/api/token/verify/', data={'token': token})
    return response.status_code == 200


def refresh_token(refresh_token):
    response = requests.post('http://example.com/api/token/refresh/', data={'refresh_token': refresh_token})
    if response.status_code == 200:
        new_access_token = response.json().get('access_token')
        update_env_file(new_access_token)
        return new_access_token
    else:
        return None


def update_env_file(access_token):
    with open('.env', 'w') as f:
        f.write(f"ACCESS_TOKEN={access_token}\n")


access_token = os.getenv("ACCESS_TOKEN")

if access_token and verify_token(access_token):
    print("Привет, мир")
else:
    refresh_token = os.getenv("REFRESH_TOKEN")
    if refresh_token:
        new_access_token = refresh_token(refresh_token)
        if new_access_token:
            print("Токен обновлен")
            print("Привет, мир")
        else:
            print("Ошибка обновления токена")
    else:
        print("Требуется авторизация")
