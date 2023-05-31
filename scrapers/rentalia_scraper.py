# Selenium scraping, Rentalia Spider by Marc Louzán 

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By
import unidecode
#import numpy as np
#from email import header

class Rentalia_Scraper:
  
  implicitlyWaitTime = 2  # Timing variables
  sleepTime = 2
  sleep = True

  def __init__(self):
    
    self.options = webdriver.ChromeOptions() # Chrome driver config
    #self.options.add_argument('--headless')
    self.options.add_argument('--no-sandbox')
    #options.add_argument("user-data-dir=selenium")
    self.options.add_argument("--remote-debugging-port=9222")
    self.options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(executable_path = r"C:\\Users\\marcl\\drivers\\chromedriver_win32\\chromedriver.exe", options = self.options) # Setting webdriver, path where driver is installed (driver version must be the same as browser version)
    #self.driver.maximize_window()                                                                                                  # and the options.
    self.actions = ActionChains(self.driver) # ActionChains (mouse and keyboard simulator)


  def Start_Rentalia_Driver(self): # Accessing to the main url and cookies
    
    url = "https://es.rentalia.com/" 
    self.driver.implicitly_wait(self.implicitlyWaitTime)
    self.driver.get(url) 
    self.Sleep()
    self.driver.implicitly_wait(self.implicitlyWaitTime)
    cookies = self.driver.find_element(By.XPATH, '//*[text()="Aceptar y cerrar"]') #Accept cookies button
    self.actions.move_to_element(cookies).click().perform()

  def Render(self): # Scrolling function for accessing to all webelements desired
    
    for i in range(1,22):
      self.actions.send_keys(Keys.SPACE).perform()
    for i in range(1,192):
      self.actions.send_keys(Keys.UP).perform()

  def Sleep(self): # Sleep time to have enough time to load the content
   
    if self.sleep == True:
      time.sleep(self.sleepTime)

  def Extract_Properties_To_CSV(self): # Scrapìng property interest fields
        loc = "España"
        link_text = unidecode.unidecode(loc).lower()

        self.driver.implicitly_wait(self.implicitlyWaitTime)
        try:
            input_field = self.driver.find_element(By.XPATH, '//*[@id="masterContainer"]/div/div[1]/div/form/div/div[1]/span/input') # Input field
        except:
            input_field = self.driver.find_element(By.CLASS_NAME, 'locationInput') 

        self.actions.move_to_element(input_field).click().send_keys(loc).perform() # Sending the location to the input field
        self.Sleep()
        self.actions.move_to_element(input_field).click().perform()
        self.Sleep()
        srch_btn = self.driver.find_element(By.CLASS_NAME, 'searchButton.waves-effect.waves-light.btn') # Clicking search button 
        self.actions.move_to_element(srch_btn).click().perform()
        self.Sleep()
      
        headers = ['Título','Ubicación','Número referencia','Precio','Capacidad','Habitaciones','Camas','Baños','Link','Teléfono móvil'] # First row of the document
        with open(f'rentalia.csv','w+', encoding = 'utf-8', newline='') as f:
          wr = csv.writer(f, dialect = 'excel')
          wr.writerow(headers)

          property_count = 0
          i= 1 # Index pagination
          while i < 525: # Total pages
              for a in range(0, 15):  # Properties per page
                self.Render()
                self.driver.implicitly_wait(self.implicitlyWaitTime)
                try:
                  prop = self.driver.find_elements(By.CLASS_NAME, 'itemContent')[a]
                except:
                  continue
                
                print(f"\n---------- PROPERTY Nº {property_count:05d} --------------")
                
                # Getting property fields 
                try:
                  title = prop.find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'h3').text
                  print("TITLE: ", title)
                except:  
                  title = ''    
                try:  
                  lctn = prop.find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME,'a').find_element(By.TAG_NAME, 'h4').text
                  print("LOCATION: ", lctn)
                except:
                  lctn = ""    
                try:
                  link = prop.find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME, 'a').get_attribute('href')
                  print("LINK: ", link)
                except:  
                  link = ''   
                try:
                  reference = link.split('/')
                  ref = reference[3]
                  print("REFERENCE NUMBER: ", ref)
                except:  
                  ref = ''   
                try:
                  price = prop.find_element(By.CLASS_NAME, 'price').find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text.split(' p')[0]
                  print("PRICE: ", price)
                except:  
                  price = ''   
                  
                self.driver.get(link) # In this case, to extract the phone number we have to move the driver again so we set the link we recently declared and go to the particular property page.
                self.Render()
                
                try:
                  capacity = self.driver.find_elements(By.CLASS_NAME, 'characteristic')[0].find_element(By.TAG_NAME, 'p').text
                  print("CAPACITY: ", capacity)
                except:
                  capacity = ''

                try:
                  rooms = self.driver.find_elements(By.CLASS_NAME, 'characteristic')[1].find_element(By.TAG_NAME, 'p').text
                  print("HABITACIONES: ", rooms)
                except:
                  rooms = ''

                try:
                  camas = self.driver.find_elements(By.CLASS_NAME, 'characteristic')[2].find_element(By.TAG_NAME, 'p').text
                  print("CAMAS: ", camas)
                except:
                  camas = ''

                try:
                  baños = self.driver.find_elements(By.CLASS_NAME, 'characteristic')[3].find_element(By.TAG_NAME, 'p').text
                  print("BAÑOS: ", baños)
                except:
                  baños = ''
              
                try:
                  tel = self.driver.find_element(By.CLASS_NAME, 'owner').find_element(By.CLASS_NAME, 'editButtons').find_elements(By.TAG_NAME, 'a')[0].text.split(" ")[1]
                  print("TELEFONO: ", tel)
                except:
                  tel = ''    

                print("-------------------------------------------")
                
                line = [title, lctn, ref, price, capacity, rooms, camas, baños, link, tel] 
                wr.writerow(line) # Adding property fields at the csv file
                  
                if i == 1:
                  self.driver.implicitly_wait(self.implicitlyWaitTime)
                  self.driver.get(f"https://es.rentalia.com/alquiler-vacaciones-{link_text}/")# Getting out to return to property list panel if first page
                else:
                  self.driver.implicitly_wait(self.implicitlyWaitTime)
                  self.driver.get(f"https://es.rentalia.com/alquiler-vacaciones-{link_text}_page_{i}/")# Getting out to return to property list panel
                
                property_count = property_count + 1
              
              i = i + 1
              self.driver.implicitly_wait(self.implicitlyWaitTime)
              self.driver.get(f"https://es.rentalia.com/alquiler-vacaciones-{link_text}_page_{i}/") # Once scraped all 15 properties of the page, moving to the next page
        
          self.driver.close() # Once finished the scraping the driver and csv file are closed
          f.close()



def main():
  scraper = Rentalia_Scraper()
  scraper.Start_Rentalia_Driver()
  scraper.Extract_Properties_To_CSV()


if __name__ == "__main__":
    main()