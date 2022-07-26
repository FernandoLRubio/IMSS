from selenium import webdriver
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

class Tarifa:
    def __init__(self,mes:int,basico:float,intermedio:float,excedente:float):
        self.mes = mes
        self.basico = basico
        self.intermedio = intermedio
        self.excedente = excedente

    def __str__(self) -> str:
        return f"Tarifa de Consumo para el mes {self.mes}:\n Básico: {self.basico}\n Intermedio: {self.intermedio}\n Excedente: {self.excedente}"

    def toJSON(self) -> str:
        return json.dumps(self.__dict__)

def obtener_tarifa(mes:int) -> Tarifa:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(30)

    driver.get("https://app.cfe.mx/Aplicaciones/CCFE/Tarifas/TarifasCRECasa/Tarifas/Tarifa1.aspx")
    month_select = driver.find_element("name","ctl00$ContentPlaceHolder1$MesVerano1$ddMesConsulta")
    drop = Select(month_select)
    drop.select_by_value(str(mes))
    driver.implicitly_wait(10)
    data = driver.find_element("id","ContentPlaceHolder1_TemporadaFV").text
    driver.quit()
    
    clean_table = data.replace("           ",",")
    clean_table = clean_table.replace("\n",",")
    split_table = clean_table.split(",")

    return Tarifa(mes,float(split_table[1]),float(split_table[4]),float(split_table[7]))
