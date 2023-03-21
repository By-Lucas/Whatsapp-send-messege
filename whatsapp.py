import datetime
import time
import webbrowser as web
from urllib.parse import quote

from pyautogui import click, hotkey, press, size, typewrite
from platform import system
import pyautogui as pg

'''pip install pyautogui'''


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
        image_path: str,
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
        image_1 = pg.locateOnScreen('images/1.png', confidence=0.9, grayscale=True, limit=10)
        pg.click(image_1)
        time.sleep(1)
        
        image_2 = pg.locateOnScreen('images/2.png', confidence=0.9, grayscale=True, limit=10)
        pg.click(image_2)
        pg.write(image_path)
        
        time.sleep(1)
        pg.press("enter")
        
        time.sleep(3)
        pg.press("enter")
        
        print('Mensagem enviada para : ',phone_no)
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
    
    message = ''
    contacts = []
    
    with open('mensagem.txt', 'r', encoding='utf-8') as f:
        message = f.read()
    
    with open('contatos.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    
    for contact in contacts:
        send_msg.Send_msg_instant(
                phone_no='+55'+contact, 
                message=message, 
                image_path='imagem.png',
                wait_time=4, 
                tab_close=True, 
                close_time=3
            )
        time.sleep(7)