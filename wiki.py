from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("log-level=2")
def wikibusca(palavra):
    documento = open("pesquisa.txt","w")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com.br/search?q="+palavra)
    sleep(3)
    info = driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/span[1]').text
    documento.write(info)
    return info

