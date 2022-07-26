from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

def obtener_multas(placas:str,numeroSerie:str) -> str:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(30)

    driver.get("https://gobiernoenlinea1.jalisco.gob.mx/serviciosVehiculares/adeudos?")
    placas_field = driver.find_element("name","placa")
    placas_field.send_keys(placas)
    serial_field = driver.find_element("name","numeroSerie")
    serial_field.send_keys(numeroSerie)
    submit_button = driver.find_element("id","btnConsultar")
    submit_button.click()
    time.sleep(2)
    raw = driver.page_source
    driver.quit()
    page = BeautifulSoup(raw,"lxml")
    dom = page.find(class_ = "ng-binding")
    try:
        total = dom.text.split(':')[1][2:]
    except:
        total = "0"
    return total