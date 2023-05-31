
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By
import unidecode
import random
import string
from PIL import Image, ImageFilter
from paddle import paddle



class Habitaclia_Scraper:
   
   implicitlyWaitTime = 1  # Timing variables
   sleepTime = 1
   sleep = True
    
    #Provinces
   provincias = ["Girona", "Barcelona", "Tarragona", "Castellón", "Valencia", "Alicante", "Madrid"]  
   #Comarcas
   zonas_girona = ["Alt Empordà", "Baix Empordà", "Gironès", "Selva", "Cerdanya"]
   zonas_barcelona = ["Maresme", "Barcelonès", "Baix Llobregat", "Garraf"]
   zonas_tarragona = ["Baix Penedès", "Tarragonès", "Baix Camp", "Baix Ebre", "Montsià"]
   zonas_castellon = ["Baix Maestrat", "Plana Alta", "Plana Baixa"]
   zonas_valencia = ["Camp de Morvedre", "Horta Nord", "Valencia", "Ribera Baixa", "Safor"]
   zonas_alicante = ["Marina Alta", "Marina Baixa", "l'Alicanti", "Baix Vinalopó", "Vega Baja"]
   zonas_madrid = ["Madrid Capital"]
   comarcas = {
      "Girona": zonas_girona, 
      "Barcelona": zonas_barcelona,
      "Tarragona": zonas_tarragona,
      "Catellón": zonas_castellon,
      "Valencia": zonas_valencia,
      "Alicante": zonas_alicante,
      "Madrid": zonas_madrid
   }
   
   def __init__(self):
     
      self.options = webdriver.ChromeOptions()
      #options.add_argument('--headless')
      #options.add_argument('--no-sandbox')
      self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
      # options.add_argument("user-data-dir=selenium")
      self.options.add_argument("--remote-debugging-port=9222")
      self.options.add_argument('--disable-dev-shm-usage')

      #C:\\Program Files\\drivers\\chromedriver.exe"
      self.driver = webdriver.Chrome(executable_path = r"C:\\Users\\marcl\\drivers\\chromedriver_win32\\chromedriver.exe", options = self.options)
      self.actions = ActionChains(self.driver) # ActionChains (mouse and keyboard simulator)

   
   def Render(self): # Scrolling function for accessing to all webelements desired
    for i in range(1,22):
      self.actions.send_keys(Keys.SPACE).perform()
    for i in range(1,192):
      self.actions.send_keys(Keys.UP).perform()

   def Sleep(self): # Sleep time to have enough time to load the content
    if self.sleep == True:
      time.sleep(self.sleepTime)
      
   def Random_char(y):
      return ''. join(random. choice(string. __all__) for x in range(y))

               
   def Read_Captcha(self):
      self.driver.implicitly_wait(self.implicitlyWaitTime)
      captcha_image = self.driver.find_element(By.XPATH, '//*[@id="js-contact"]/div/div[1]/div[1]/form/fieldset/label[5]/img')
      captcha_image.screenshot('captcha.png')
      img = Image.open('captcha.png')
      text = paddle.paddle.reader(img)
      return text
   
   def Start_Habitaclia_Driver(self):
      self.driver.get("https://www.habitaclia.com/")
      self.driver.maximize_window()

      self.driver.implicitly_wait(self.implicitlyWaitTime)
      cookies_btn = self.driver.find_element(By.XPATH, '//*[@id="legalCookies"]/div/div/div/footer/div/button[2]')
      self.actions.move_to_element(cookies_btn).click().perform()

      self.driver.implicitly_wait(self.implicitlyWaitTime)
      venta = self.driver.find_element(By.ID, "tip_op").find_element(By.XPATH, '//*[text()="Comprar"]')
      self.actions.move_to_element(venta).click().perform()

      self.driver.implicitly_wait(self.implicitlyWaitTime)
      tipo = self.driver.find_element(By.ID, "tip_inm").find_element(By.XPATH, '//*[text()="Vivienda"]')
      self.actions.move_to_element(tipo).click().perform()
  
   def Extract_Results(self):

      headers = ['Portal', 'Tipo','Título','Ubicación','Precio','Superfície','Habitaciones','Baños','Valor','Link','Teléfono móvil']
      with open('habitaclia.csv','w+', encoding = 'utf-8', newline='') as file:
       wr = csv.writer(file, dialect = 'excel')
       wr.writerow(headers)  
       for prov in self.provincias:
         
         self.driver.implicitly_wait(self.implicitlyWaitTime)
         prov_actual = self.driver.find_element(By.ID, "cod_prov").find_element(By.XPATH, f'//*[text()="{prov}"]')
         self.actions.move_to_element(prov_actual).click().perform()
         time.sleep(5)
         
         self.driver.implicitly_wait(self.implicitlyWaitTime)
         buscar = self.driver.find_element(By.CLASS_NAME, "botonazul.buscar")
         self.actions.move_to_element(buscar).click().perform()
         time.sleep(5)
         
         for comarca in self.comarcas[prov]:
            
            self.driver.implicitly_wait(self.implicitlyWaitTime)
            com_actual =self.driver.find_element(By.XPATH, f'//*[text()="{comarca}"]')
            com_text = com_actual.text
            if " " in com_text:
               s = com_text.replace(" ", "_").lower()
               out_text = unidecode.unidecode(s)
            else:
               out_text = unidecode.unidecode(com_text).lower()
            
            self.actions.move_to_element(com_actual).click().perform()
            
            self.driver.implicitly_wait(self.implicitlyWaitTime)
            search_link = self.driver.find_element(By.CLASS_NAME, "ver-todo-zona")
            self.actions.move_to_element(search_link).click().perform()
            
            
            #10 pages foreach comarca.   
            i = 0
            while i < 10:
             for a in range(0, 15): #15 properties per page
                  
               self.driver.implicitly_wait(self.implicitlyWaitTime)
               try:
                  link_prop = self.driver.find_elements(By.CLASS_NAME, 'list-item-info')[a].find_element(By.CLASS_NAME, 'list-item-title').find_element(By.TAG_NAME, 'a')
                  lctn = self.driver.find_elements(By.CLASS_NAME, 'list-item-info')[a].find_element(By.CLASS_NAME, 'list-item-location').text
               except:
                  continue

               link = link_prop.get_attribute('href')

               self.actions.move_to_element(link_prop).click().perform()
               self.Sleep()

               self.Render()
               
         
               try:
                  title = self.driver.find_element(By.CLASS_NAME, 'summary-left').find_element(By.TAG_NAME, 'h1').text
                  print("TÍTULO: ",title)
               except:  
                  title = ''  
               
               print("UBICACIÓN: ", lctn)
               
               try:  
                  precio = self.driver.find_element(By.CLASS_NAME, 'summary-left').find_element(By.CLASS_NAME,'price').find_element(By.TAG_NAME, 'span').text
                  print("PRECIO: ", precio)
               except:
                  precio = ""   

               self.driver.implicitly_wait(self.implicitlyWaitTime)
               try:
                  features =  self.driver.find_element(By.ID, 'js-feature-container').find_elements(By.CLASS_NAME, 'feature')      
               except:
                  continue
               try:
                  superficie = features[0].text
                  print("SUPERFÍCIE: ", superficie)
               except:  
                  superficie = ''   
               try:
                  habitaciones = features[1].text
                  print("HABITACIONES: ", habitaciones)
               except:  
                  habitaciones = ''  
               try:
                  baños = features[2].text
                  print("BAÑOS: ", baños)
               except:  
                  baños = ''  
               try:
                  valor = features[3].text
                  print("VALOR M*2: ", valor)
               except:  
                  valor = '' 
               
                         
               # EL SIGUIENTE PASO ES EL PROCESO PARA EXTRAER EL TELEFONO MOBIL, LO OMITO PORQUE ES ILEGAL YA QUE HAY QUE HACER CAPTCHA LO CUAL PUEDO HACER PORQUE ES SENCILLO.
               
               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # input_nombre = self.driver.find_element(By.ID, 'solicitudesForm').find_element(By.ID, 'etiquetanombre').find_element(By.TAG_NAME, 'input')
               # random_name = self.Random_char(9)
               # self.actions.move_to_element(input_nombre).click().perform()
               # input_nombre.send_keys(random_name)

               # random_number = random.randrange(600500000, 750000000)
               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # input_movil = self.driver.find_element(By.ID, 'solicitudesForm').find_element(By.ID, 'etiquetatel').find_element(By.TAG_NAME, 'input')
               # self.actions.move_to_element(input_movil).click().perform()
               # input_movil.send_keys(random_number)

               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # input_email = self.driver.find_element(By.ID, 'solicitudesForm').find_element(By.ID, 'etiquetaemail').find_element(By.TAG_NAME, 'input')
               # email = self.Random_char(8) + "@gmail.com"
               # self.actions.move_to_element(input_email).click().perform()
               # input_email.send_keys(email)
               

               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # input_text = self.driver.find_element(By.ID, 'solicitudesForm').find_element(By.ID, 'divCaptcha').find_element(By.ID, 'CaptchaInputText')
               # self.actions.move_to_element(input_text).click().perform()
               # input_text.send_keys(self.Read_Captcha())
            
               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # z = self.driver.find_element(By.ID, 'idBtnCerrar')
               # self.actions.move_to_element(z).click().perform()


               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # terms = self.driver.find_element(By.ID, 'solicitudesForm').find_elements(By.CLASS_NAME, 'w-100.f-left.contact-options')
               # first = terms[0].find_element(By.ID, 'idLabelRecibirAlertas').find_element(By.CLASS_NAME, 'tiny-span')
               # self.actions.move_to_element(first).click().perform()
               # self.Sleep()
               # second = terms[0].find_element(By.ID, 'idLabelLegalContactar').find_element(By.CLASS_NAME, 'tiny-span')
               # self.actions.move_to_element(second).click().perform()
               # self.Sleep()
               
               # self.driver.implicitly_wait(self.implicitlyWaitTime)
               # new_code = self.driver.find_element(By.ID, 'solicitudesForm').find_element(By.ID, 'divCaptcha').find_element(By.ID, 'reloadCaptcha')
               # self.actions.move_to_element(new_code).click().perform()
               # tries = tries + 1
            
               
               
               # contact_btn = terms[1].find_element(By.TAG_NAME, 'input')
               # self.actions.move_to_element(contact_btn).click().perform()

                  
               try:
                phone = self.driver.find_element(By.CLASS_NAME, 'contactotelf').find_element(By.CLASS_NAME, 'tel-llamar')
                print(phone)
               except:
                phone = ""
               
               #mark = mark + 1

               print("------------------")

               #Adding all item fields to the csv file as a line
               line = [title, lctn, precio, superficie, habitaciones, baños, valor, link, phone]   
               self.Sleep()
               wr.writerow(line)
               
               #Getting out to return to property list page
               
               try:
                if i == 0:
                  self.driver.implicitly_wait(10)
                  self.driver.get(f"https://www.habitaclia.com/viviendas-en-{out_text}.htm")
                  self.Sleep()
                else:
                  self.driver.implicitly_wait(10)
                  self.driver.get(f"https://www.habitaclia.com/viviendas-en-{out_text}-{i}.htm")
                  self.Sleep()
               
               except:
                  self.driver.implicitly_wait(10)
                  back_menu = self.driver.find_element(By.ID, "js-header-container").find_element(By.ID, "js-head-back")
                  self.actions.move_to_element(back_menu).click().perform()
                  self.Sleep()
            
             # When all properties page are extracted we move to next page
             i = i + 1
             self.driver.implicitly_wait(self.implicitlyWaitTime)
             self.driver.get(f"https://www.habitaclia.com/viviendas-en-{out_text}-{i}.htm")
             self.Sleep()
                  
             
                  
            #When all comarca properties done
            print("Comarca done")
            print("Loading next comarca")
            url= (f"https://www.habitaclia.com/comprar-vivienda-en-{prov}/buscador.htm")
            self.driver.implicitly_wait(self.implicitlyWaitTime)
            self.driver.get(url)
               

         #When we complete all comarcas of actual provincia
         print("Provincia done")
         print("Back to Main Menu")
         url= "https://www.habitaclia.com/"
         self.driver.implicitly_wait(self.implicitlyWaitTime)
         self.driver.get(url)
         
       self.driver.close()
       file.close()  


def main():
  scraper = Habitaclia_Scraper()
  scraper.Start_Habitaclia_Driver()
  scraper.Extract_Results()


if __name__ == "__main__":
    main()