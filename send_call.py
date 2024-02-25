import os
import requests
from dotenv import load_dotenv
import sys

load_dotenv()


def verify_token(token):
    response = requests.post('http://127.0.0.1:8000/api/token/verify/', data={'token': token})
    return response.status_code == 200


def refresh_token(refresh):
    response = requests.post('http://127.0.0.1:8000/api/token/refresh/', data={'refresh': refresh})
    if response.status_code == 200:
        access = response.json().get('access')
        with open('.env', 'w') as f:
            f.write(f"REFRESH_TOKEN={refresh}\n")
            f.write(f"ACCESS_TOKEN={access}\n")
        return access
    else:
        return None


def login(login, password):
    response = requests.post('http://127.0.0.1:8000/api/login/', data={'username': login, 'password': password})
    access = response.json().get('access')
    refresh = response.json().get('refresh')

    if response.status_code == 200:
        with open('.env', 'w') as f:
            f.write(f"REFRESH_TOKEN={refresh}\n")
            f.write(f"ACCESS_TOKEN={access}\n")

        return access


def send_call(caller, receiver, recording, access):
    with open(recording, 'rb') as file:
        url = 'http://127.0.0.1:8000/api/call/create/'
        files = {'recording': file}
        headers = {'Authorization': f'Bearer {access}'}
        requests.post(url, data={'caller': caller, 'receiver': receiver}, files=files, headers=headers)


def main(caller, receiver, recording):
    access_token = os.getenv("ACCESS_TOKEN")

    if access_token and verify_token(access_token):
        send_call(caller, receiver, recording, access_token)
    else:
        refresh = os.getenv("REFRESH_TOKEN")
        if refresh and verify_token(refresh):
            access = refresh_token(refresh)
        else:
            access = login('admin', 'admin')

        send_call(caller, receiver, recording, access)


if __name__ == '__main__':
    args = sys.argv
    main(args[1], args[2], args[3])
