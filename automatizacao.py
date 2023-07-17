from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

def automatizar_paginas(enderecos_ip):
    # Configurar as opções do Microsoft Edge
    edge_options = Options()
    edge_options.add_argument("--ignore-certificate-error")

    # Inicializar o driver do Microsoft Edge com as opções configuradas
    driver = webdriver.Edge(options=edge_options)

    for ip in enderecos_ip:
        try:
            # Acessar página
            driver.get("https://" + ip + "/")

            # Liberação de segurança
            driver.find_element(By.ID, 'details-button').click()
            driver.find_element(By.ID, 'proceed-link').click()

            time.sleep(2)

            # Dados de LOGIN
            driver.find_element(By.ID, 'uname').send_keys('admin')
            driver.find_element(By.ID, 'psw').send_keys('M1814@0815')

            # Clicar no botão de login
            driver.find_element(By.XPATH, '/html/body/form/div[1]/div[3]/button').click()

            time.sleep(3)

            # Verificar se o elemento IP Configuration está presente
            ip_config_element = driver.find_element(By.ID, 'IPConfiguration')
            
            if ip_config_element.is_displayed():
            
                # Clicar no IP CONFIGURATION
                ip_config_element.click()
                # Clicar no IP CONFIGURATION
                driver.find_element(By.ID, 'IPConfiguration').click()

                time.sleep(1)

                # Clicar no Services
                driver.switch_to.frame(0)  # Entrar no iframe
                driver.find_element("xpath", "/html/body/form/table/tbody/tr/td[1]/div[1]/table/tbody[9]/tr/td").click()
                time.sleep(1)

                # Preencher Servers
                driver.find_element(By.ID, 'TLSSRVR').clear()
                driver.find_element(By.ID, 'TLSSRVR').send_keys('xsp.gc.italk.net.br')
                driver.find_element(By.ID, 'TLSDIR').clear()
                driver.find_element(By.ID, 'TLSDIR').send_keys('dms/Avaya_J100/')

                # Preencher dados usuário http
                driver.find_element(By.ID, 'HTTP_AUTH_USERNAME').clear()
                driver.find_element(By.ID, 'HTTP_AUTH_USERNAME').send_keys('avayadms')
                driver.find_element(By.ID, 'HTTP_AUTH_PASSWORD').clear()
                driver.find_element(By.ID, 'HTTP_AUTH_PASSWORD').send_keys('v01C3@Manager')

                # Salvar e aguardar 5 segundos
                driver.find_element("xpath", '/html/body/form/table/tbody/tr/td[1]/div[2]/span/input[1]').click()
                driver.switch_to.default_content()  # Sair do iframe
                time.sleep(5)

            else:
                # Executar o caminho alternativo fornecido
                # Reset
                driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[1]/ul/li[17]/a').click()

                # Aguardar o alerta e aceitar
                driver.switch_to.alert.accept()

        # Continua execução caso haja erro em uma página
        except Exception as e:
            print(f"Erro ao processar o IP {ip}: {str(e)}")
            continue

    driver.quit()