from datetime import datetime
import os, requests

def get_public_ip() -> str:
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    return ip

def log(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")

    file_size_limit = 5 * 1024
    

    if os.path.exists("log.txt"):

        if os.path.getsize("log.txt") > file_size_limit:
            with open("log.txt", "w") as log_file:
                log_file.write(f"[{now}] {message}\n")

        with open("log.txt", "a") as log_file:
            log_file.write(f"[{now}] {message}\n")
    else:
        with open("log.txt", "w") as log_file:
            log_file.write(f"[{now}] {message}\n")