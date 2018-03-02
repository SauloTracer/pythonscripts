from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
'''
options.add_argument("--no-startup-window")
options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions'
'''
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(360)

driver.get("https://portal.dataprev.gov.br/situacao-concursados/2016?field_candidato_value=&field_cargo_value=&field_perfil_value=DESENVOLVIMENTO&field_lotacao_value=RIO+DE+JANEIRO&field_cadastro_reserva_value=&field_inscricao_value=&field_cpf_value=&op-concurso=Pesquisar")

x = driver.find_element_by_xpath("//*[@id='block-system-main']/div/div/div[3]/table/tbody/tr[17]/td[9]")
#y = driver.find_elements_by_xpath("//td[text()='ADMITIDO']")
y = driver.find_element_by_xpath("//*[@id='block-system-main']/div/div/div[3]/table/tbody")

status = x.text
qtdAprovados = 0

for row in y.find_elements_by_tag_name('tr')[:]:
    if (row.find_elements_by_tag_name("td")[8].text == 'ADMITIDO'):
        qtdAprovados += 1

print(x.text, qtdAprovados)

driver.stop_client()
driver.close()
driver.quit()
driver = None
