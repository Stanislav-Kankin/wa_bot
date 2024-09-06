import pywhatkit
from config import PHONE


def send_message():
    pywhatkit.sendwhatmsg_instantly(PHONE, "Приветулечки")


def main():
    send_message()


if __name__ == "__main__":
    main()
