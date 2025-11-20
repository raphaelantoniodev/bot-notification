from selenium.webdriver.chrome.options import Options
from functions.login import login
from selenium import webdriver
from time import sleep

def Bot():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--start-maximized')
    options.add_argument(r"--user-data-dir=C:\SeleniumCache\project") ## salva cache de login whatsapp para não precisar relogar

    driver = webdriver.Chrome(options=options)

    print(r"""
    _______                       __                            __         ______              __                          __           
    |       \                     |  \                          |  \       /      \            |  \                        |  \          
    | $$$$$$$\  ______    ______  | $$____    ______    ______  | $$      |  $$$$$$\ _______  _| $$_     ______   _______   \$$  ______  
    | $$__| $$ |      \  /      \ | $$    \  |      \  /      \ | $$      | $$__| $$|       \|   $$ \   /      \ |       \ |  \ /      \ 
    | $$    $$  \$$$$$$\|  $$$$$$\| $$$$$$$\  \$$$$$$\|  $$$$$$\| $$      | $$    $$| $$$$$$$\\$$$$$$  |  $$$$$$\| $$$$$$$\| $$|  $$$$$$\
    | $$$$$$$\ /      $$| $$  | $$| $$  | $$ /      $$| $$    $$| $$      | $$$$$$$$| $$  | $$ | $$ __ | $$  | $$| $$  | $$| $$| $$  | $$
    | $$  | $$|  $$$$$$$| $$__/ $$| $$  | $$|  $$$$$$$| $$$$$$$$| $$      | $$  | $$| $$  | $$ | $$|  \| $$__/ $$| $$  | $$| $$| $$__/ $$
    | $$  | $$ \$$    $$| $$    $$| $$  | $$ \$$    $$ \$$     \| $$      | $$  | $$| $$  | $$  \$$  $$ \$$    $$| $$  | $$| $$ \$$    $$
    \$$   \$$  \$$$$$$$| $$$$$$$  \$$   \$$  \$$$$$$$  \$$$$$$$ \$$       \$$   \$$ \$$   \$$   \$$$$   \$$$$$$  \$$   \$$ \$$  \$$$$$$ 
                        | $$                                                                                                             
                        | $$                                                                                                             
                        \$$                                                                                                                                                                                                            

    system developer
    """)

    login(driver)

while True:
    Bot()
    sleep(18000)