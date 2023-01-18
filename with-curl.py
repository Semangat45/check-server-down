import os
import time
import schedule


def get_command_output(command: str):
    command_output = os.popen(command).read()
    return command_output


def curl_command(url: str):
    return f"curl -I {url} | grep HTTP"


def process_output(output: str) -> str:
    if "HTTP" not in output:  # presumably request timeout
        return "RTO"

    # output should be something like: "HTTP/2 200"
    status_code = output.split()[1]
    if status_code != "200":  # if not 200, it means either redirected or error
        return status_code

    return "200"


def job():
    url = "https://www.google.com"
    command = curl_command(url)
    output = get_command_output(command)
    status = process_output(output)

    print(status + " => " + url)


def schedule_job():
    schedule.every().minute.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    job()
