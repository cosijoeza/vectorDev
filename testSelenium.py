#Librarys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from fpdf import FPDF
import random
import time
import string

# Log in 
def login(user,password):
    print("LOG IN")
    try:
        #email
        idEmail = 'input#email'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,idEmail))).send_keys(user)

        #password
        idPassword = 'input#password'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,idPassword))).send_keys(password)

        #wait for vectordev to be ready
        time.sleep(2)

        #Login button
        buttonClass = 'button.MuiButtonBase-root MuiButton-root'.replace(' ','.')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,buttonClass))).click()

        #Wait for vectordev to be ready
        time.sleep(10)

        return True
    except:
        driver.get(url)
        print("*LOG IN TEST FAILED")

        return False

# Log out
def logout():
    print("LOG OUT")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Click on menu
        buttonPath = '/html/body/div/div/div/div[1]/div[4]/button'
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        
        #Click on log out
        buttonPath = '/html/body/div/div/div/div[1]/div[4]/div/div/ul/a[2]'
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        return True
    except:
        driver.get(url)
        print("*LOG OUT TEST FAILED")

        return False

#Add Unit
def addUnit():
    print("ADD UNIT")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Add unit button
        buttonPath = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/button[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Unit type button
        buttonPath = '/html/body/div[2]/div[3]/div/div[2]/div/div/div/div/div'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Select Unit type
        buttonPath = '/html/body/div[3]/div[3]/ul/li[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        
        #Dispenser type button
        buttonPath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[1]/div/div'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        
        #Select random dispenser type
        item = random.randint(0,2)+1
        buttonPath = '/html/body/div[3]/div[3]/ul/li['+ str(item) +']'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Generate random serial number
        id = 'TEST_'+ str( random.randint(0,10000) )
        letter = ''
        for i in range (3):
            letter += random.choice(string.ascii_letters)
        id += letter

        #Write serial number
        serialNumber = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[2]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

        #Write IoTecha PCBA serial number
        PCBA = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[3]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,PCBA))).send_keys('abcdef12345678')

        #Write BeagleBone Serial number
        beagleSerial = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[4]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,beagleSerial))).send_keys('abcdef12345678')

        #SIM Card number
        sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[5]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('abcdef12345678')
        
        #Has modem CHECK
        modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/label/span[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()

        #Write CradlePoint IMEI
        sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[6]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('abcdef12345678')

        #Write CradlePoint MAC
        sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[7]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('abcdef12345678')

        #Write VectorStatSerial
        sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[1]/div[8]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('abcdef12345678')
        
        time.sleep(5)
        
        #Click on save
        modem = '/html/body/div[2]/div[3]/div/div[2]/form/div/div[2]/div/button[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,modem))).click()
        
        time.sleep(10)
        print("New id: ",id)
        print("TEST PASSED\n--------------------------")
        return id
    except:
        print("ADD UNIT TEST FAILED\n--------------------------")
        driver.get(url)
        time.sleep(5)
        return False

def deleteUnit(id):
    print("DELETE UNIT")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Search Unit by id
        serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

        #Click on first unit
        unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        #Edit unit
        unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        #Click on delete
        unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        if id == 'RD201174':
            #Cancel
            buttonPath = '/html/body/div[2]/div[3]/div/div[3]/button[1]'
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
            #Save update
            buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/button[2]'
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        else:
            #Confirm    
            buttonPath = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()


        print("Unit ",id," was deleted")
        print("TEST PASSED\n--------------------------")
        time.sleep(10)
        return True
    except :
        driver.get(url)
        print("TEST FAILED\n--------------------------")

        return False

def updateUnit(id):
    print("UPDATE UNIT")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Search Unit added
        serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id))

        #Click on unit searched
        unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        time.sleep(2)

        #Edit unit
        unit = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        #Choose random option
        item = random.randint(0,2)+1
        buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        

        #Choose random option
        item = random.randint(0,2)+1
        buttonPath = '/html/body/div[2]/div[3]/ul/li['+ str(item) +']'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        
        #Write a description
        sim = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[4]/div/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('Update unit test')
        

        #Save update
        buttonPath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/button[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()
        
        time.sleep(10)
        
        print("TEST PASSED\n--------------------------")

        return True
    except:
        driver.get(url)
        print("TEST FAILED\n--------------------------")

        return False

def addUnitNotes(id):
    print("ADD UNIT NOTES")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Search Unit added
        serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id)) 

        #Click on unit searched
        unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        time.sleep(2)

        #View notes
        notePath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

        #Write a note
        sim = '/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[1]/div/textarea[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,sim))).send_keys('Selenium Test note 3')

        time.sleep(5)
        
        #Click on Add button
        notePath = '/html/body/div[2]/div[3]/div/div[2]/form/div/div/div[2]/div/button[2]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

        time.sleep(10)

        #Close pop up
        notePath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

        print("TEST PASSED\n--------------------------")

        return True
    except:
        driver.get(url)
        print("TEST FAILED\n--------------------------")
        return False

def viewUnitNotes(id):
    print("VIEW UNIT NOTES")
    try:
        #Unit top button
        buttonPath = '/html/body/div/div/div/div[1]/header/div/div/div/a[1]'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,buttonPath))).click()

        #Search Unit added
        serialNumber = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/thead/tr[2]/th[1]/input'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,serialNumber))).send_keys(str(id)) 

        #Click on unit searched
        unit = '/html/body/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/a'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,unit))).click()

        time.sleep(2)

        #View notes
        notePath = '/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()

        time.sleep(10)

        #Close pop up
        notePath = '/html/body/div[2]/div[3]/div/div[1]/h2/div/button'
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,notePath))).click()
        
        print("TEST PASSED\n--------------------------")
        
        return True
    except:
        driver.get(url)
        print("TEST FAILED\n--------------------------")
        return False

def pdfReport(resultsList):
    #Permission list
    permissions = [
        [True, True, True, True, True],
        [False, False, False, False, False],
        [False, True, False, True, True],
        [True, True, True, True, True],
        [False, True, False, True, True],
        [False, False, False, False, False]
    ]

    #PDF format
    pdf = FPDF(orientation = 'L', unit = 'mm',format = 'A4')
    pdf.add_page()
    pdf.set_font('Arial','',12)

    #Begin to create PDF
    name = 'datyra-logo.png'
    pdf.image(name,10,10,60,20)
    pdf.ln(30)
    pdf.multi_cell(0,10,'The next table shows the results obtained after performing tests with Selenium.',
    'Cell values = Has permissions : Test result ')
    pdf.ln(5)

    #Create table
    pdf.set_font('Arial','B',12)
    pdf.cell(w=280,h=15,txt='Test Report',ln=1,border = 1 ,align='C',fill=0)

    users = ['','SysAdmin','UserAdmin','Field Service ','EOL Tech','Engineering','Customer']
    descriptions = ['Add Unit','Update Unit','Add Unit Notes','View Unit Notes','Delete Unit']
    
    width = 40
    for user in users:
        pdf.cell(w=width,h=15,txt=user,border = 1 ,align='C',fill=0)
    
    pdf.set_font('Arial','',12)
    pdf.ln(15)

    text = ''
    for i in range(len(descriptions)):
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial','B',12)
        pdf.cell(w=width,h=15,txt=descriptions[i],border = 1 ,align='C',fill=0)
        
        pdf.set_font('Arial','',12)
        for j in range(len(users)-1):
            result = permissions[j][i]
            if result == True:    
                text = 'Yes'
            else:
                text = 'No'

            if result == resultsList[j][i]:
                pdf.set_text_color(8,130,21)
                text += ' : Succesful'        
            else:
                pdf.set_text_color(255,0,0)
                text += ' : Failure'        
            pdf.cell(w=width,h=15,txt=text,border = 1 ,align='C',fill=0)
        pdf.ln(15)

    #PDF's name
    pdf.output('testResults.pdf')

string.ascii_letters
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/home/cosi/Descargas/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options=options)

url = 'http://localhost:3000/'
url='http://vectordev.vectorstat.com/'

driver.get(url)

users = [
    'sysadmin@test.com',
    'useradmin@test.com',
    'fieldservice@test.com',
    'eoltech@test.com',
    'engineering@test.com',
    'customersupport@test.com'
]
passwords = [
    'sysadmin@test.com',
    'useradmin@test.com',
    'fieldservice@test.com',
    'eoltech@test.com',
    'engineering@test.com',
    'customersupport@test.com'
]

resultsList = []
testResult = []
for i in range(len(users)):
    #i = 2
    #i = len(users)-1    
    print("User: ",users[i],"Password: ",passwords[i])
    login(users[i],passwords[i])

    idG = 'RD201174'    
    
    id = addUnit()
    driver.refresh()
    #Si no se crea una nueva unidad, debemos probar con una que ya esté creada para testaer los metodos
    if id == False:
        testResult.append(id)
        id = idG
    else:
        testResult.append(True)
    print("ID: ",id)
    testResult.append(updateUnit(id))
    testResult.append(addUnitNotes(id))
    testResult.append(viewUnitNotes(id))
    time.sleep(10)
    testResult.append(deleteUnit(id))
    time.sleep(10)
    logout()
    print("***************\n")
    resultsList.append(testResult)
    testResult = []
    #break

print(resultsList)
pdfReport(resultsList)



"""
Las que no tengan EPROM no se pueden editar hasta que se den de alta en REDIS
NO SE PUEDE AGREGAR 'BBB Eprom'

Los permisos debemos traerlos desde la base de datos

No existen permisos para EOL Tech

Oscar pedir que copie la tabla de rol permisos copiarlo a dev role y role permissions

"""