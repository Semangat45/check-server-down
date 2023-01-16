from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


def print_title(url: str):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # option not to open browser
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        # error 502 (nginx), will print: 502 Bad Gateway
        print(driver.title)

    except WebDriverException:  # request timeout will be catched in this exception
        print("Webdriver exception / possibly RTO")

    driver.close()


if __name__ == '__main__':
    print_title("https://google.com")


