from proxy_dz import socks5, clear
from colorama import init, Fore

""" Iniciar Colorama """
init()

print("ฅ•ω•ฅ")
print("Repo: https://github.com/j3andz/proxy_dz\n")


def main():
    """Menú del Script para elejir que tipo de Proxy correr"""
    print("Menú:\n\n1- Proxy Socks5\n2- Proxy Socks4\n3- Proxy HTTP\n4- About")
    dz = int(input("= "))
    if dz == 1:
        active_socks5()
    elif dz == 2:
        active_socks4()
    elif dz == 3:
        active_http()
    elif dz == 4:
        about()


def active_socks5():
    """Correr Proxy SOCKS5 con seguridad o sin ella"""
    clear()
    print("Socks5 Type:\n1- Open Proxy\n2- Secure Proxy")
    type = int(input(""))
    if type == 1:
        clear()
        port = int(input("Puerto: "))
        socks5(port)
    elif type == 2:
        clear()
        username = input("Usuario: ")
        password = input("Contraseña: ")
        port = int(input("Puerto: "))
        socks5(port, username, password)


def active_socks4():
    """Correr Proxy SOCKS4, pero aún no está disponible, espero ayuda de la comunidad"""
    clear()
    print("socks4")


def active_http():
    """Correr Proxy HTTP, pero aún no está disponible, espero ayuda de la comunidad"""
    clear()
    print("http")


def about():
    clear()
    print(
        Fore.RED
        + """Proyecto: proxy_dz 

Canal de Telegram: https://t.me/j3an_dz

Usuario de Telegram: https://t.me/j3andz

Comunidad: https://t.me/PixelDZ

"""
    )


input()

if __name__ == "__main__":
    main()
