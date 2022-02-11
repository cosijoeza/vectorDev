#Librarys
from lib2to3.pgen2 import driver
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
            print(e+"in getPermissions in userTestClass")
 
    # Add new logo
    def addLogo(self):
        self.historyTestOrder.append("AddLogo")
        print("ADD LOGO")
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
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #add Logo
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Select random organization
            item = random.randint(0,13)+1
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Generate random serial number and letter
            string.ascii_letters 
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            id = 'LOGOTEST_'+ str( random.randint(0,10000) )
            letter = ''
            for i in range (3):
                letter += random.choice(string.ascii_letters)
            id += letter

            #Name
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(str(id))

            #Description
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[3]/div/input'
            dateNow = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys("Test Description ",str(dateNow))

            #Upload 600x150px 
            picturePath = "/home/cosi/Imágenes/logo_test.png"
            #self.driver.find_element_by_id("contained-button-file1").send_keys("/home/cosi/Documentos/datyra/test/selenium/Nuvve-Rhombus-480x125.png")
            self.driver.find_element_by_id("contained-button-file1").send_keys(picturePath)

            #Upload 90x60px 
            self.driver.find_element_by_id("contained-button-file2").send_keys("/home/cosi/Documentos/datyra/test/selenium/Nuvve-Rhombus-55x45.png")

            time.sleep(5)

            #Save
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("\nin addLogo")
            self.driver.get(self.url)
            print("TEST FAILED\n--------------------------")
            return False

    # Add a new unit in VectorStat
    def addUnit(self):
        self.historyTestOrder.append("AddUnit")
        print("ADD UNIT")
        try:
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Add unit button
            buttonPath = '//*[@id="root"]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/button[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Unit type button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Select Unit type
            buttonPath = '/html/body/div[3]/div[3]/ul/li[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Dispenser type button
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Select random dispenser type
            item = random.randint(0,2)+1
            buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Generate random serial number and letter
            string.ascii_letters 
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            id = 'RD'+ random.choice(string.ascii_letters.upper()) + str( random.randint(200000,1000000) ) + '_TEST'

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
            if check == 1:
                #Has modem CHECK
                modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/label/span[1]'
                WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()

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
            
            time.sleep(10)
            
            #Click on save
            modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[2]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()
            time.sleep(5)

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
            sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[1]/div/textarea[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('Test note written at ')

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
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Select organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Click on first option
            buttonPath = '/html/body/div[3]/div[3]/ul/li'
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
            item = random.randint(0,1)
            print("WP: ")
            if item == 0:
                print("20.8kB")
            else:
                print("1.1MB")
            picturePath = '/home/cosi/Documentos/datyra/test/selenium/picture_profile_test['+str(item)+'].png'
            self.driver.find_element_by_id("imageinput").send_keys(picturePath)

            #Select role
            item = random.randint(0,6)+1
            print(item)
            buttonPath= '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/div[1]/div[2]/fieldset/div/label['+str(item)+']/span[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            time.sleep(7)

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

            #Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

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

    # Generate a PDF file (report's results of test)
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

    # Compare actions user performed during test against actions database gives
    def hasPermission(self,history):
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
            #Unit top button
            buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Click on menu button
            buttonPath = '/html/body/div/div/div/div[1]/div[4]/button'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            
            #Click on log out button
            buttonPath = '/html/body/div/div/div/div[1]/div[4]/div/div/ul/a[2]'
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            return True
        except Exception as e:
            print(e)
            self.driver.get(self.url)
            print("LOG OUT TEST FAILED")
            return False

    # Update logo
    def updateLogo(self,name):
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

            #Logos
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Search logo
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Click on logo name
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(2)
            
            #Update
            self.driver.find_element_by_xpath('//div[@id="logoEdit"]/*[name()="svg"]').click()
            
            #New description
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[3]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys("Updated logo")
            
            item = random.randint(0,1)
            print(item)
            if item == 1:
                #Upload 600x150px 
                self.driver.find_element_by_id("contained-button-file1").send_keys("/home/cosi/Documentos/datyra/test/selenium/big-logo.png")
            else:
                #Upload 90x60px 
                self.driver.find_element_by_id("contained-button-file2").send_keys("/home/cosi/Documentos/datyra/test/selenium/little-logo.png")

            time.sleep(5)

            #Save
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/form/div[5]/div/button[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Close logo window
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
    
    # Update a unit from Vectorstat
    def updateUnit(self,id):
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

            time.sleep(5)

            #Edit unit
            unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

            #Product type
            buttonPath = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            #Choose random option
            item = random.randint(0,2)+1
            buttonPath = '/html/body/div[2]/div[3]/ul/li['+ str(item) +']'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Beaglebone Serial #
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys('abc..|123')

            #Screen Brightness
            item = random.randint(0,8) * 10 + 20
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/input'
            element = self.driver.find_element_by_xpath(buttonPath).clear()
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(item)

            #Poll Intervals (seconds)
            item = random.randint(0,54) * 10 + 60
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/input'
            element = self.driver.find_element_by_xpath(buttonPath).clear()
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[6]/div/input'
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
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[1]/div/nav/div[5]/div/div/div/div/div'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Description
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).send_keys(name)

            #Click on logo name
            buttonPath = '/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/span'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

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
    
    # View unit notes in Vectorstat
    def viewUnitNotes(self,id):
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

            #Select organization
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/select/option'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Select role
            buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[2]/fieldset/div/select/option'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            time.sleep(10)

            #Close pop up
            buttonPath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

            #Wait while information is saving
            time.sleep(10)

            print("TEST PASSED\n--------------------------")
            return True
        except Exception as e:
            print(e)
            print("VIEW USER TEST FAILED\n--------------------------")
            self.driver.get(self.url)
            time.sleep(5)
            return False    
