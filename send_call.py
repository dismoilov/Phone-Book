import os
import requests
from dotenv import load_dotenv
import sys
import wave

load_dotenv()


def get_audio_duration(file_path):
    with wave.open(file_path, 'rb') as audio_file:
        num_frames = audio_file.getnframes()
        frame_rate = audio_file.getframerate()
        duration = num_frames / frame_rate

        return duration


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
        if len(caller) > 6 and len(receiver) < 6:
            status = 'Inbound'
        elif len(caller) < 6 and len(receiver) > 6:
            status = 'Outbound'
        else:
            status = 'Local'

        requests.post(url, data={'caller': caller, 'receiver': receiver, 'recording': recording, 'status': status},
                      headers=headers, files=files)


def main(caller, receiver, recording):
    if get_audio_duration(recording) >= 3:
        access_token = os.getenv("ACCESS_TOKEN")

        if access_token and verify_token(access_token):
            send_call(caller, receiver, recording, access_token)
        else:
            refresh = os.getenv("REFRESH_TOKEN")
            if refresh and verify_token(refresh):
                access = refresh_token(refresh)
            else:
                access = login('admin', '!Qazxsw2')

            send_call(caller, receiver, recording, access)


if __name__ == '__main__':
    args = sys.argv
    main(args[1], args[2], args[3])
