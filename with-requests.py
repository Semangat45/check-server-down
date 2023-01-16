import requests  # pip install requests
import schedule  # pip install schedule
import time


def print_status_code(url: str):
    try:
        req = requests.get(url, verify=False)
        print(req.status_code)
    except requests.exceptions.ConnectTimeout:
        print("RTO")


def job():
    print_status_code("https://google.com")


def schedule_job():
    schedule.every().minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_job()
