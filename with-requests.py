import requests  # pip install requests


def print_status_code(url):
    try:
        req = requests.get(url, verify=False)

        print(req.status_code)
    except requests.exceptions.ConnectTimeout:
        print("RTO")


if __name__ == "__main__":
    print_status_code("https://google.com")
