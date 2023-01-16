import os
import time

import schedule


def print_from_command(command: str):
    p = os.popen(command).read()
    print(p)


def job():
    print_from_command("curl -I https://google.com | grep HTTP")


def schedule_job():
    schedule.every().minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    schedule_job()
