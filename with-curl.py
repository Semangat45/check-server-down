import os


def print_os_command(command: str):
    p = os.popen(command).read()
    print(p)


if __name__ == '__main__':
    print_os_command("curl -I https://google.com | grep HTTP")
