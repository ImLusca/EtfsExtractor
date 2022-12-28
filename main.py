from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://www.etfsbrasil.com.br/rankings")

buttons = browser.find_elements(By.XPATH, '//button[contains(text(), "Ver todos")]')

for btn in buttons:
    btn.click()

tables = browser.find_elements(By.TAG_NAME, 'table')

# Aqui vc pode extrair por linha ou da forma que quiser
for tab in tables:
    val = tab.text
    print(val)