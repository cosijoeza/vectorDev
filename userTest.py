#Librarys
from lib2to3.pgen2 import driver
from pandas import DatetimeIndex
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from fpdf import FPDF
import psycopg2.extras
import psycopg2 
import random
import string
import time
from datetime import datetime

class vectorStat:
    def __init__(self):
        self.idUnit = ""
        self.historyTestOrder = []
        self.actions = []
        self.CONN = None
        self.CUR = None   
    # Add new logo
    def addLogo(self):
        self.historyTestOrder.append("AddLogo")
        print("ADD LOGO")
        try:
            # Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[1]/div/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Add Logo
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Select random organization
            item = random.randint(0,13)+1
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Generate random serial number and letter
            string.ascii_letters 
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            id = 'LOGO'+ random.choice(string.ascii_letters.upper()) + str( random.randint(200000,1000000) ) + '_TEST'
            #Name
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(str(id))

            # Description
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[3]/div'
            dateNow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys("Test Description ",str(dateNow))

            # Upload small logo
            option = random.randint(0,1)
            picturePath = "/home/cosi/Documentos/datyra/test/selenium/logoPictures/logo_picture["+str(option)+"].png"
            #self.driver.find_element_by_id("contained-button-file1").send_keys("/home/cosi/Documentos/datyra/test/selenium/Nuvve-Rhombus-480x125.png")
            self.driver.find_element_by_id("contained-button-file1").send_keys(picturePath)

            # Upload big logo  
            option = random.randint(2,3)
            picturePath = "/home/cosi/Documentos/datyra/test/selenium/Nuvve-Rhombus-55x45.png"
            self.driver.find_element_by_id("contained-button-file2").send_keys(picturePath)

            time.sleep(5)

            #Save
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            print(id+" added")
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin addLogo")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Add organization
    def addOrganitzation(self):
        self.historyTestOrder.append("AddOrganization")
        print("ADD ORGANIZATION")
        try:
            # Go Home            
            buttonPath = '/html/body/div/div/div/div[1]/div[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Go to organizations
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Add organization
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[3]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Organization name
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[1]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Addres
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div[1]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Contact name
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # City
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Contact Email
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # State
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Phone
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Zip
            stringInformation = "--"
            inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div[4]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(stringInformation))

            # Select role
            item = random.randint(1,3)
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/div[1]/fieldset/div/select/option['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            time.sleep(7)

            # Save button
            buttonPath='/html/body/div[2]/div[3]/div/div[2]/form/div[3]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()


            print(id," added\nTEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("ADD ORGANIZATION TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
    
    # Add Role
    def addRole(self):
        self.historyTestOrder.append("addRole")
        print("ADD ROLE")
        try:
            # Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to vectorDev load information
            time.sleep(10)
            
            # Click on roles option
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[2]/a '
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to vectorDev load information
            time.sleep(5)
            
            # Add role
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[2]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Display organizations option
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Select random dispenser type
            item = random.randint(1,13)
            print(item)
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Generate random role name
            string.ascii_letters 
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys("Role-"+random.choice(string.ascii_letters.upper())+" Test")

            # Description
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys("Description-"+random.choice(string.ascii_letters.upper()))
            
            #   Select permissions
            for i in range(random.randint(1,60)):
                inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[6]/div['+str(random.randint(1,60))+']/label/span[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).click()
            
            time.sleep(15)

            # Save button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[7]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(5)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("ADD ROLE TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False

    #Add software component
    def addSoftwareComponent(self):
        self.historyTestOrder.append("AddSoftwareComponent")
        print("ADD SOFTWARE COMPONENT")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Software components
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Add component
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Component type
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Choose component type
            option = random.randint(1,5)
            inputPath = '/html/body/div[3]/div[3]/ul/li['+str(option)+']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).click()

            #Select picture .img
            picturePath = '/home/cosi/Imágenes/20220510-rel9.8.img'
            #self.driver.find_element_by_id("").send_keys(picturePath)

            # Release notes
            length_of_string = 2000
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[4]/div/textarea[1]'
            text = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length_of_string))
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(text)

            # Cancel
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/div/button[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Confirm to cancel
            buttonPath = '/html/body/div[3]/div[3]/div/div[2]/button[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Save information            
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/div/button[2]'
            #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(5)
            return True
        except Exception as e:
            print(e)
            print("\nin add Software Component")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Add a new unit in VectorStat
    def addUnit(self,option):
        self.historyTestOrder.append("AddUnit")
        print("ADD UNIT")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            time.sleep(3)            
            #Add unit button
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Unit type button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Generate random serial number and letter
            string.ascii_letters 
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            id = 'RD'+ random.choice(string.ascii_letters.upper()) + str( random.randint(200000,1000000) ) + '_TEST'

            if option == 1:
                #Select Unit type (Dispenser)
                buttonPath = '/html/body/div[3]/div[3]/ul/li[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                
                #Dispenser type button
                buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[1]/div/div'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                
                #Select random dispenser type
                item = random.randint(0,2)+1
                buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                #Write serial number
                serialNumber = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[2]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

                #Write IoTecha PCBA serial number
                PCBA = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[3]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,PCBA))).send_keys('--')

                #Write BeagleBone Serial number
                beagleSerial = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[4]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,beagleSerial))).send_keys('--')

                number = random.randint(200000,1000000)
                #SIM Card number
                sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[5]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys(str(number))
                
                check = random.randint(0,1)
                print("Has modem? ",check)
                #Has modem CHECK
                modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/label/span[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()
                if check == 1:
                    number = random.randint(200000,1000000)
                    #Write CradlePoint IMEI
                    sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[6]/div/input'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys(str(number))

                    number = random.randint(200000,1000000)
                    #Write CradlePoint MAC
                    sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[7]/div/input'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys(str(number))

                    #Write VectorStatSerial
                    sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[8]/div/input'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys(str(id))
                
                time.sleep(5)
            elif option == 2:
                #Select Unit type (PCS)
                buttonPath = '/html/body/div[3]/div[3]/ul/li[2]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                #Select PCS type
                buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[1]/div/div'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                #Select random dispenser type
                item = random.randint(1,5)
                buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                #PCS Serial Number
                inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[2]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(id))

                check = random.randint(0,1)
                print("Has No AC Energy? ",check)
                #0: NO
                #1: YES
                if check == 1:
                    #Unit Has No AC Energy Meter Serial Number
                    checkBox = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/label/span[1]'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,checkBox))).click()
                else:
                    #AC Energy Meter Serial Number
                    number = random.randint(200000,1000000)
                    inputButton = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[3]/div/input'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputButton))).send_keys(str(number))
                    
            time.sleep(5)
            
            #Click on save
            modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[2]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()
            #Close                                  
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            #WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,modem))).click()

            self.driver.refresh()
            self.driver.get(self.url)
            self.id = id
            print(id," added\nTEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("ADD UNIT TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False

    # Add a note in a unit            
    def addUnitNote(self,id):
        self.historyTestOrder.append("AddUnitNotes")
        print("ADD UNIT NOTES")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Search Unit added
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id)) 

            #Click on unit searched
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            time.sleep(2)

            #View notes
            notePath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

            #Write a note
            now  = datetime.now()
            sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[1]/div/textarea[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('Test note written at '+str(now.hour)+':'+str(now.minute))

            time.sleep(5)
            
            #Click on Add button
            notePath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[2]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

            time.sleep(10)

            #Close pop up
            notePath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Add new user
    def addUser(self,name,lastName,email):
        self.historyTestOrder.append("addUser")
        print("ADD USER")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Clic on user option
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Add user
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Select organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Select option
            option = random.randint(1,14)
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+str(option)+']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            print("Name: ",name," ",lastName,"Email: ", email)
            #Name
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Last Name
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(lastName)

            #Email
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[4]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(email)
            
            #Upload picture
            item = random.randint(0,2)
            if item == 0:
                print("20.8kB")
            else:
                print("1.1MB")
            picturePath = '/home/cosi/Documentos/datyra/test/selenium/profilePictures/picture_profile_test['+str(item)+'].png'
            self.driver.find_element_by_id("imageinput").send_keys(picturePath)
            """
            #Select role
            item = random.randint(1,7)
            print(item)
            buttonPath= '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/div[1]/div[2]/fieldset/div/label['+str(item)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            time.sleep(7)
            """
            #Save button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[3]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Wait to vectorDev save information
            time.sleep(10)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("ADD USER TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
 
    # Clear user permission list from database
    def clearPermissionListFromDB(self): 
        self.permissionsFromDB = []

    # User actions history
    def clearHistory(self):
        self.historyTestOrder = []  

    # Delete logo
    def deleteLogo(self,name):
        self.historyTestOrder.append("DeleteLogo")
        print("DELETE LOGO")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(5)
            
            #Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[1]/div/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(8)
            #Search logo
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Click on logo name
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(2)

            #Update
            self.driver.find_element_by_xpath('//div[@id="logoEdit"]/*[name()="svg"]').click()

            #Delete logo
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Confirm
            buttonPath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Close logo window
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin deleteLogo")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False 

    # Delete a unit from Vectorstat
    def deleteUnit(self,id):
        self.driver.get(self.url)
        self.historyTestOrder.append("DeleteUnit")
        print("DELETE UNIT")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Search Unit by id
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

            #Click on first unit
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #Edit unit
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #Click on delete
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            if id == 'RD201024':
                #Cancel button
                buttonPath = '/html/body/div[2]/div[3]/div/div[3]/button[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                #Save update
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/button[2]'
                #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            else:
                #Confirm button 
                buttonPath = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()


            print("Unit ",id," was deleted")
            print("TEST PASSED\n--------------------------")
            time.sleep(10)
            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Generate a PDF file (reports results of test)
    def generateReport(self,resultsList,correctPermissions,users):

        users.insert(0,'')
        testedActions = self.historyTestOrder

        #PDF format
        pdf = FPDF(orientation = 'L', unit = 'mm',format = 'A4')
        pdf.add_page()
        pdf.set_font('Arial','',12)

        #Begin to create PDF
        name = 'datyra-logo.png'
        pdf.image(name,10,10,60,20)
        pdf.ln(30)
        pdf.multi_cell(0,10,'The next table shows the results obtained after performing tests with Selenium.\nCell values = Has permissions : Test result ')
        pdf.ln(5)

        #Create table
        pdf.set_font('Arial','B',12)
        pdf.cell(w=280,h=15,txt='Test Report',ln=1,border = 1 ,align='C',fill=0)
        #Print users
        width = 40
        for user in users:
            pdf.cell(w=width,h=15,txt=user,border = 1 ,align='C',fill=0)
        #pdf.set_font('Arial','',12)
        pdf.ln(15)

        #Write into the table
        text = ''
        for j in range(len(testedActions)):
            #Print testedActions
            pdf.set_text_color(0,0,0)
            pdf.set_font('Arial','B',12)
            pdf.cell(w=width,h=15,txt=testedActions[j],border = 1 ,align='C',fill=0)
            
            #Write test results
            #We subtract 1 to skip the action we just wrote
            pdf.set_font('Arial','',12)
            for i in range(len(users)-1):
                result = correctPermissions[i][j]
                if result == True:    
                    text = 'Yes'
                else:
                    text = 'No'
                if result == resultsList[i][j]:
                    pdf.set_text_color(8,130,21)
                    text += ' : Succesful'        
                else:
                    pdf.set_text_color(255,0,0)
                    text += ' : Failure'        
                pdf.cell(w=width,h=15,txt=text,border = 1 ,align='C',fill=0)
            pdf.ln(15)

        #PDF's name
        pdf.output('testResults.pdf')

    # Access methods
    def getEmail(self):
        return self.email

    def getIdUnit(self):
        return self.id
    
    def getHistoryTestOrder(self):
        return self.historyTestOrder

    # Permission list user has in vectorstatDB
    def getPermissions(self):
        try: 
            #Get id role by email
            query = "SELECT id_role FROM \"authorization\".\"user\" WHERE email ='" + self.email +"'"
            print(query)
            self.CUR.execute(query)
            result = self.CUR.fetchone()
            key = result[0]
            self.CONN.commit()

            #Get permissions user have
            query = """SELECT pms.name AS permission FROM \"authorization\".\"role\" AS r
            INNER JOIN \"authorization\"."role_permission" AS rp ON r.id = rp.id_role
            INNER JOIN "authorization"."permission" AS pms ON pms.id = rp.id_permission
            WHERE rp.id_role ='""" + str(key)+"'"
            self.CUR.execute(query)
            permissions  = self.CUR.fetchall()
            self.CONN.commit()

            self.CUR.close()
            self.CONN.close()
            return [item for sublist in permissions for item in sublist]
        except Exception as e:
            print(e+" in getPermissions in userTestClass")

    # Compare actions user performed during test against actions database gives
    def hasPermission(self,history):
        try:
            #We look for the action in the database
            self.permissionsFromDB = self.getPermissions()
            results = []
            permissionList = [x.lower() for x in self.permissionsFromDB]
            history = [x.lower() for x in history]
            for i in history:
                if i in permissionList:
                    results.append(True)
                else:
                    results.append(False)
            return results
        except Exception as e:
            print(e+" in hasPermission in userTestClass")

    # Log In to VectorStat
    def logIn(self):
        print("LOG IN")
        try:
            #write email
            idEmail = 'input#email'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,idEmail))).send_keys(self.email)

            #write password
            idPassword = 'input#password'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,idPassword))).send_keys(self.password)

            #wait for vectordev to be ready
            time.sleep(2)

            #click on Login button
            buttonClass = 'button.MuiButtonBase-root MuiButton-root'.replace(' ','.')
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,buttonClass))).click()

            #Wait for vectordev to be ready
            time.sleep(15)

            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("LOG IN TEST FAILED")
            return False
    
    # Log Out from VectorStat
    def logOut(self):
        print("LOG OUT")
        try:
            self.driver.get(self.url)
            time.sleep(5)
            
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Click on menu button
            buttonPath = '/html/body/div/div/div/div[1]/div[4]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Click on log out button
            buttonPath = '/html/body/div/div/div/div[1]/div[4]/div/div/ul/a'
            WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("LOG OUT TEST FAILED")
            return False

    # Diagnostic test
    def runCommunicationTest(self,id):
        self.historyTestOrder.append("runCommunicationTest")
        print("RUN COMMUNICATION TEST")
        try:
            # Go to home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Units top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Search unit
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

            # Click on unit searched
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            # Display diagnostic tests
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/nav/div[4]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # Click on run manual tests
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/nav/div[5]/div/div/div/div[1]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # Wait page is loading
            time.sleep(5)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin runCommunicationTest")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Diagnostic test
    def runManualTest(self,id):
        self.historyTestOrder.append("runManualTest")
        print("RUN MANUAL TEST")
        try:
            # Go to home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Units top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Search unit
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

            # Click on unit searched
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            # Wait while unit is loading
            time.sleep(5)

            # Display diagnostic tests
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/nav/div[4]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # Click on run manual tests
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[1]/div/nav/div[5]/div/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #   ---PART ONE---

            # 1. Select dielectric test option
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[1]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 2. Component ID's Verification
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[2]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 3. Component ID's Verification
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[3]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 4. Screen Test 
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[4]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 5. VectorStat Software Version
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[5]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 6. IoTecha Connectivity (IoT.ON Portal)
            option = random.randint(1,3)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/fieldset[6]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            time.sleep(10)

            # Click on next button
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/form/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #   ---PART TWO---
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 7. IoTecha Firmware Version
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[1]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            # 8. MODBUS Communication Test
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[2]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 9. Bender Settings Verification
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[3]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            # 10. Check for relay operation on IMD board.
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[4]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 11. Vehicle Charging Test
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[5]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 12. AC Meter Reading is Operational
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/fieldset[6]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            time.sleep(10)

            # Click on next button
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/span/div/form/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #   ---PART THREE---
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/button[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # EPO Test
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/span/div/form/fieldset[1]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 14.-IMI Test
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/span/div/form/fieldset[2]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 15. GMI Test 
            option = random.randint(1,2)
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/span/div/form/fieldset[3]/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # 16. Comments
            inputPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/span/div/form/div[1]/div/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys("Test comments")

            time.sleep(10)

            # Click on complete button
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/span/div/form/div[2]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin runManualTest")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Access methods
    def setConecction(self,driver,url):
        self.driver = driver
        self.url = url

    def setSession(self,email,password):
        self.email = email
        self.password = password

    def setEmail(self,newEmail):
        self.email = newEmail

    def setPassword(self,newPassword):
        self.password = newPassword

    def setDbConecction(self,db_name, db_user, db_password, db_host):
        try:
            self.CONN = psycopg2.connect(dbname=db_name, user=db_user, password = db_password,host=db_host)
            self.CUR = self.CONN.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            print(e," in setDBConecction")
 
    # Update logo
    def updateLogo(self,name,active = None):
        self.driver.get(self.url)
        if active != None:
            self.historyTestOrder.append("UpdateLogoStatus")
            print("UPDATE LOGO STATUS")
        else:
            self.historyTestOrder.append("UpdateLogo")
            print("UPDATE LOGO")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(5)

            #Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[1]/div/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(8)
            #Search logo
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Click on logo name
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(2)
            
            #Update
            self.driver.find_element_by_xpath('//div[@id="logoEdit"]/*[name()="svg"]').click()
            if active == None:
                #New description
                buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/input'            
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys("Updated logo")
                
                item = random.randint(0,1)
                if item == 1:
                    #Upload 600x150px 
                    self.driver.find_element_by_id("contained-button-file1").send_keys("/home/cosi/Documentos/datyra/test/selenium/logoPictures/logoPicture[3].png")
                else:
                    #Upload 90x60px 
                    self.driver.find_element_by_id("contained-button-file2").send_keys("/home/cosi/Documentos/datyra/test/selenium/logoPictures/logoPicture[1].png")
                print("logo updated: "+str(item))
                time.sleep(5)

            else:
                if active == False:
                    # Record Status
                    buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[2]/div/div/div'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                    # Inactive
                    buttonPath='/html/body/div[3]/div[3]/ul/li[2]'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                else:
                    # Record Status
                    buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[2]/div/div/div'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                    # Active
                    buttonPath='/html/body/div[3]/div[3]/ul/li[1]'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()                 

            #Save
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[4]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin updateLogo")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False
    
    # Update organization
    def updateOrganization(self,organization):
        self.historyTestOrder.append("updateOrganization")
        print("UPDATE ORGANIZATION")
        try:
            # Go Home            
            buttonPath = '/html/body/div/div/div/div[1]/div[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Go to organizations
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Search organization
            inputPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(organization)

            # Click on organization searched
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to see details
            time.sleep(3)

            # Edit organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/div[1]/div/svg/svg'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Wait to page is loading
            time.sleep(10)
            
            # Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Wait to page is loading
            time.sleep(10)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("UPDATE ORGANIZATION TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
    
    def updateRole(self,roleName):
        self.historyTestOrder.append("updateRole")
        print("UPDATE ROLE")
        try:
            # Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to vectorDev load information
            time.sleep(10)
            
            # Click on roles option
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[2]/a '
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to vectorDev load information
            time.sleep(5)
            print(roleName)
            
            #Write role name in search textbox
            inputPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(str(roleName))

            #Click on fisrt result
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Click on update button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/div[1]/div/svg'
            #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            time.sleep(10)

            #Select organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[1]/div[1]/div/div'
            #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Choose random option
            item = random.randint(0,14)
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Role name
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[1]/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys('*')

            #Description
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[1]/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys('*')

            time.sleep(10)
            for i in range(10):
                item = random.randint(1,57)
                checkBox ='/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[3]/div[2]/div[2]/div['+str(item)+']/label/span[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,checkBox))).click()
            
            time.sleep(15)
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("UPDATE ROLE TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
    
    # Update software component
    def updateSoftwareComponent(self,imageName,active = None):
        self.historyTestOrder.append("updateSoftwareComponent")
        print("UPDATE SOFTWARE COMPONENT")
        try:
            # Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Software components
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Search by image name
            inputPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[2]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(str(imageName))

            # Choose the first one
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Edit button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div/div[3]/div/svg[1]/svg'
            #WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Release notes
            length_of_string = 2000
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div[4]/div/div/textarea[1]'            
            text = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length_of_string))
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(str(text))

            time.sleep(15)
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("UPDATE SOFTWARE COMPONENT\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False

    # Update a unit from Vectorstat
    def updateUnit(self,id,active = None):
        self.driver.get(self.url)
        if active != None:
            self.historyTestOrder.append("UpdateUnitStatus")
            print("UPDATE UNIT STATUS")
        else:
            self.historyTestOrder.append("UpdateUnit")
            print("UPDATE UNIT")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Search Unit added
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

            #Click on unit searched
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()
            
            #Wait while unit is loading
            time.sleep(5)

            #Edit unit
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            # Active or deactive unit
            if active != None:
                #Record status
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/p/div/div/div'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                if active == True:
                    buttonPath = '/html/body/div[2]/div[3]/ul/li[1]'
                else: 
                    buttonPath = '/html/body/div[2]/div[3]/ul/li[2]'
                time.sleep(5)
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click() 

                #Save update
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/button[2]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                
                #Confirmation to deactivate unit
                if active == False:
                    # Yes
                    buttonPath = '/html/body/div[2]/div[3]/div/div[2]/button[2]'
                    # No
                    buttonPath = '/html/body/div[2]/div[3]/div/div[2]/button[1]'
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            else:
                #Product type
                buttonPath = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
                
                #Choose random option
                item = random.randint(1,3)
                buttonPath = '/html/body/div[2]/div[3]/ul/li['+ str(item) +']'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

                #Beaglebone Serial #
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys('abc..|123')

                #Screen Brightness
                item = random.randint(2,10) * 10
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(item)

                #Poll Intervals (seconds)
                item = random.randint(1,6) * 100
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[5]/div/input'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(item)  

                #Save update
                buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/button[2]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            time.sleep(10)
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False
  
    # Update user
    def updateUser(self,email,active = None):
        self.historyTestOrder.append("updateUser")
        print("UPDATE USER")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Write in email search box
            inputText = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[3]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputText))).send_keys(str(email))
            
            time.sleep(5)
            
            # click on first result
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[3]/span/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            time.sleep(5)
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Update user
            #buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[1]/svg/svg'
            self.driver.find_element_by_xpath('//div[@id="userEdit"]/*[name()="svg"]').click()

            # Update first name
            inputText = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/input'
            self.driver.find_element_by_xpath(inputText).clear()   
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputText))).send_keys("UPD")

            # Update last name
            inputText = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[3]/div/input'
            self.driver.find_element_by_xpath(inputText).clear()
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputText))).send_keys("UPD")
            
            # Email
            inputPath = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[4]/div/input'
            self.driver.find_element_by_xpath(inputText).clear()
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys("UPD")

            # Record status
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[5]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Change to active or inactive
            if active:
                buttonPath = '/html/body/div[3]/div[3]/ul/li[1]'
            else:
                buttonPath = '/html/body/div[3]/div[3]/ul/li[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Roles
            option = random.randint(1,12)
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div[1]/fieldset/div/label['+str(option)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Profile picture
            option = random.randint(0,1)
            print("option--> "+str(option))
            picturePath = "/home/cosi/Documentos/datyra/test/selenium/profilePictures/picture_profile_test["+str(option)+"].png"
            self.driver.find_element_by_id("imageinput").send_keys(picturePath)

            
            # time to review information
            time.sleep(10)
            # Save button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div[3]/button[2]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("UPDATE USER TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
    
    # View logo
    def viewLogo(self,name):
        self.historyTestOrder.append("ViewLogo")
        print("VIEW LOGO")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Lookup table maint
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[4]/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div[1]/div/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Description
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Click on logo name
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Time to view logo information
            time.sleep(5)

            #Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin updateLogo")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # View organization
    def viewOrganization(self,organization):
        self.historyTestOrder.append("viewOrganization")
        print("VIEW ORGANIZATION")
        try:
            # Go Home            
            buttonPath = '/html/body/div/div/div/div[1]/div[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Go to organizations
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Search organization
            inputPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,inputPath))).send_keys(organization)

            # Click on organization searched
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            # Wait to see details
            time.sleep(10)

            # Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            # Wait to page is loading
            time.sleep(10)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("VIEW ORGANIZATION TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False

    # View Role
    def viewRole(self,role):
        self.historyTestOrder.append("viewRole")
        print("VIEW ROLE")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            print(role)
            time.sleep(5)
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("VIEW ROLE TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False

    # View unit notes in Vectorstat
    def viewUnitNotes(self,id):
        self.driver.get(self.url)
        self.historyTestOrder.append("ViewUnitNotes")
        print("VIEW UNIT NOTES")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Search Unit added
            serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id)) 

            #Click on unit searched
            unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            time.sleep(2)

            #View notes
            notePath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

            time.sleep(10)

            # Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # View users in Vectorstat
    def viewUser(self):
        email = 'vguluarte@rhombusenergysolutions.com'
        self.historyTestOrder.append("viewUser")
        print("VIEW USER")
        try:
            #Home
            buttonPath = '/html/body/div/div/div/div[1]/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Admin
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[3]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Click on user option
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Write in email box to search
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[3]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(email)

            #Click on search result
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr/td[3]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(10)

            #Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("VIEW USER TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False
    
    def exists():
       return True