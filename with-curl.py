import os


def print_from_command(command: str):
    p = os.popen(command).read()
    print(p)


if __name__ == '__main__':
    print_from_command("curl -I https://google.com | grep HTTP")
