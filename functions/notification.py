from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from time import sleep

def get_status_product(driver: webdriver.Chrome, number: str):
    driver.get('https://panini.com.br/box-chainsaw-man-vols-1-ao-11-achab001br')
    statusLocal = 'Indisponível'

    statusAPI = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[5]/div[4]/h5')

    price = driver.find_element(By.CLASS_NAME, 'price')

    if not statusAPI:
        statusLocal = 'Disponível para compra'

    message = f"""Olá Arthur, segue status atualizado sobre o produto.\n\n*Produto: {driver.title}*\n*Preço: {price.text}*\n*Status: {statusLocal}*\n\nSegue informações extras.\nData e hora de consulta: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}\nLink: https://panini.com.br/box-chainsaw-man-vols-1-ao-11-achab001br"""

    driver.get('https://web.whatsapp.com/')

    searchBar = '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p'

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, searchBar))
    ).send_keys(number)

    sleep(10)
    driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]').click()
    print('cliquei no perfil...')

    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]').send_keys(message)
    
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/div/span/button/div').click()
    driver.quit()