from .open import run_open_proxy
from .secure import run_secure_proxy
from .config import clear


def socks5(port, username=None, password=None):
    if username:
        secure_proxy(port, username, password)
    else:
        open_proxy(port)


def open_proxy(port):
    clear()
    run_open_proxy(port)


def secure_proxy(port, username, password):
    clear()

    run_secure_proxy(port, username, password)
