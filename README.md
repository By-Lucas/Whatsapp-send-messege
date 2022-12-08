# AUTOMATION : SEND MESSEGE WHATSAPP

~~~
import datetime
import time
import webbrowser as web
from urllib.parse import quote

from pyautogui import click, hotkey, press, size, typewrite
from platform import system
import pyautogui as pg

'''pip install pyautogui'''
'''python3 pip install pyautogui'''


class WhatsappMessage:

    def __init__(self) -> None:

        self.url = 'https://web.whatsapp.com'
        self.WIDTH, self.HEIGHT = size()
        

    def close_tab(self, wait_time: int = 2) -> None:
        """Fecha a guia do navegador aberta no momento"""

        time.sleep(wait_time)
        if system().lower() in ("windows", "linux"):
            hotkey("ctrl", "w")
        elif system().lower() == "darwin":
            hotkey("command", "w")
        else:
            raise Warning(f"{system().lower()} não suportado!")
        press("enter")


    def check_number(self, number: str) -> bool:
        """Verifica o número para ver se contém o código do país"""

        return "+" in number or "_" in number


    def Send_msg_instant(
        self,
        phone_no: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
    ) -> None:
        """Enviar mensagem WhatsApp instantaneamente"""

        if not self.check_number(number=phone_no):
            raise CountryCodeException("Código do país ausente no número de telefone!")

        web.open(f"{self.url}/send?phone={phone_no}&text={quote(message)}")
        time.sleep(4)
        #click(self.WIDTH / 2, self.HEIGHT / 2)
        time.sleep(wait_time)
        pg.press("enter")
        print(datetime.datetime.now(), phone_no, message)
        if tab_close:
            self.close_tab(wait_time=close_time)


    def open_web() -> bool:
        """Abrir o WhatsApp Web"""
        try:
            web.open("https://web.whatsapp.com")
        except web.Error:
            return False
        else:
            return True


class CountryCodeException(Exception):
    """
    Código do país ausente no número de telefone
    """
    pass


if __name__ == '__main__':
    send_msg = WhatsappMessage()

    send_msg.Send_msg_instant(
            phone_no='+5574981199190', 
            message='Oi, tudo bem?', 
            wait_time=1, 
            tab_close=True, 
            close_time=2
        )

~~~