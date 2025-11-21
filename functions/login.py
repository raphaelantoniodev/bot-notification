from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from functions.notification import get_status_product
from dotenv import load_dotenv
from selenium import webdriver
from datetime import datetime
from time import sleep
import os

load_dotenv()

def login(driver: webdriver.Chrome):
    driver.get('https://web.whatsapp.com/')
    not_logged = True

    while not_logged:
        sleep(5)
        os.system('cls')

        print('[LOGS]: Starting system.\n')

        try:
            canvas = driver.find_element(By.TAG_NAME, "canvas")
            print("[LOGS]: Checking section...")

            qr_base64 = driver.execute_script("""
                const canvas = arguments[0];
                return canvas.toDataURL('image/png').split(',')[1];
            """, canvas)

            print("\n[LOGS]: QR Code Base64 para login:")
            print(qr_base64)

        except:
            print("[LOGS]: QR não encontrado, verificando se logou...")

            try:
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
                )

                not_logged = False
                print(f'[LOGS]: Login successfully - {datetime.now().strftime("%d/%m as %H:%M")}')
                print('[LOGS]: Starting data collection system for automatic notification sending.')

                get_status_product(driver=driver, number=os.getenv("NUMBER"))
                return

            except:
                continue


