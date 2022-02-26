from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import sys
script_dir = os.path.dirname( __file__ )
gui_dir = os.path.join(script_dir, "..", "GUI")
sys.path.append(gui_dir)
import GUI.GUI as GUI

class Linkedin_autoConnect:
    def run(self, keyword, loop):
        '''
            Inicia o robô, chamando todos os metodos/funções necessarias
            :param str keyword: Palavra chave para procurar person no LinkedIn
            :param int loop: Total de person que você quer se conectar
        '''
        self.configure_selenium()
        self.open_linkedin()
        self.login()
        self.search_keyword(keyword)
        for i in range(0, int(loop)):
            self.connect_to_people()
            self.next_page()
            sleep(10)
        self.close()
    
    def close(self):
        """
        Fecha o navegador

        """
        self.driver.quit()
    
    def configure_selenium(self):
        """
            Configurações basicas para iniciar o Selenium

        """

        #Mude para o caminho do seu Chromedriver.exe
        self.working_directory = os.getcwd()
        self.driver_path = self.working_directory + r"/Data/chromedriver.exe"
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1050,768")
        self.driver = webdriver.Chrome(self.driver_path, options=self.chrome_options)
    
    def open_linkedin(self):
        """
            Abrir o site LinkedIn
        
        """
        self.driver.get("https://www.linkedin.com/")

    def login(self):
        interface = GUI.screen()
        interface.popup()


    # def login(self, usuario, senha):

    #         """
    #             Realiza o login, recebendo como parametro o usuario e senha do usuario

    #         """

    #         self.login_input =  WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "session_key")))
    #         self.login_input.send_keys(usuario)
    #         self.password_input = self.driver.find_element(By.ID, "session_password")
    #         self.password_input.send_keys(senha)
    #         self.login_button = self.driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
    #         self.login_button.click()
        
    def search_keyword(self, keyword):

        """
            Pesquisa pela palavra chave no linkedin
        """
        self.search_input_exists = WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@class="search-global-typeahead__input always-show-placeholder"]')))
        self.search_input = self.driver.find_element(By.XPATH, '//*[@class="search-global-typeahead__input always-show-placeholder"]')
        self.search_input.click()
        self.search_input.send_keys(keyword)
        self.search_input.send_keys(Keys.ENTER)
        self.filter_people_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Pessoas"]')))
        self.filter_people_button.click()

    def next_page(self):

        """
            Avança para a proxima pagina de person
        """

        self.scroll_down = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button/span[text()='Avançar']")))
        self.button.click()
    
    def connect_to_people(self):

        """
            Pega uma lista de todas as person na pagina, verifica um a um se é possivel conectar, se sim, realiza a conexão. Se não, pula a currentPerson.
        """


        self.person_exists = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//li[@class="reusable-search__result-container "]')))
        self.person = self.driver.find_elements(By.XPATH, '//li[@class="reusable-search__result-container "]')

        for self.currentPerson in self.person:
            self.nome = self.currentPerson.find_element(By.XPATH, '//span[@aria-hidden="true"]').text.split()[0]
            if self.currentPerson.find_element(By.TAG_NAME, "button").is_enabled():
                self.conectar = self.currentPerson.find_element(By.TAG_NAME, "button").click()
            else:
                print("Não foi possivel se conectar, indo para a proxima")
                continue
            if self.currentPerson.find_element(By.TAG_NAME, "button").get_attribute("aria-label") == "Seguir":
                print("Não foi possivel se conectar, indo para a proxima")
                continue
            else:
                pass

            print(f"Enviando mensagem para {self.nome}")
            sleep(5)
            self.conectar2 = self.currentPerson.find_element(By.TAG_NAME, "button")
            self.conectar2.click()
            self.adicionar_nota_exists = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Adicionar nota"]')))
            self.adicionar_nota = self.driver.find_element(By.XPATH, '//button[@aria-label="Adicionar nota"]')
            self.adicionar_nota.click()
            self.custom_message = self.driver.find_element(By.ID, "custom-message")
            self.message = f"Olá {self.nome}, tudo bem?\nMe chamo Marco e estou no 2 ano de Ciências da computação.\nPara expandir minhas conexões no LinkedIn, busco por person da área.\nFiz um robô com Python+Selenium para me ajudar nessa missão(Essa mensagem foi enviada por ele!)\nMe ajude a criar este network, obrigado :)"
            self.custom_message.send_keys(self.message)
            self.send_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Enviar agora"]')
            sleep(3)
            self.send_button.click()
            sleep(5)