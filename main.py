#Librarys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from userTest import vectorStat
import time
import os

#Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = '/home/cosi/Documentos/datyra/test/selenium/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options=options)
driver
url = 'http://localhost:3000/'
url='http://vectordev.vectorstat.com/'

users = ['']
results = []
userTestResult = [] #b
allowedUserPermission = [] #permisos permitidos para usuarios $allowedUserPermission

try:
    try:
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")
        PASSWORDS = os.getenv("PASSWORDS").split(",\n")
        USERS = os.getenv("USERS").split(",\n")
    except Exception as e:
        print(e)

    print(DB_HOST)
    print(DB_NAME)
    print(DB_USER)
    print(DB_PASS)
    print(USERS)

    driver.get(url)
    user = vectorStat()
    user.setConecction(driver,url)
    
    for i in range(len(USERS)):
        user.setSession(USERS[i],PASSWORDS[i])
        print(USERS[i])
        print(PASSWORDS[i])
        users.append(user.getEmail())
        user.clearHistory()
        
        user.logIn()
        added = user.addUnit()
        userTestResult.append(added)
        time.sleep(10)
        driver.refresh()
        id = 'RD201003' #poner razon de porque está y ponerlo en archivo de constantes
        userTestResult.append(user.updateUnit(id))
        time.sleep(5)
        userTestResult.append(user.viewUnitNotes(id))
        time.sleep(10)      
        userTestResult.append(user.addUnitNotes(id))
        time.sleep(10)
        #Comprobar si es id get id unit  
        if added:
            userTestResult.append(user.deleteUnit(user.getIdUnit()))
        else:
            userTestResult.append(user.deleteUnit(id))
        time.sleep(10)
        user.addLogo()
        time.sleep(5)
        user.viewLogo("Test logo")
        time.sleep(5)
        #user.updateLogo("Nuvve - SDGE")
        user.updateLogo("Test logo")
        time.sleep(5)
        user.deleteLogo("Test logo")
        time.sleep(5)
        user.logOut()
        results.append(userTestResult)
        userTestResult = []
        
        historyTestOrder = user.getHistoryTestOrder()
        user.setDbConecction(DB_NAME,DB_USER,DB_PASS,DB_HOST)
        verifyHistory = user.hasPermission(historyTestOrder)
        allowedUserPermission.append(verifyHistory) #$allowedUserPermissionFromDatabase
        
        
        print("History: \n{}\n".format(historyTestOrder))
        print("Permissions: \n{}".format(verifyHistory))
        
        user.clearPermissionListFromDB()

    driver.close()
    print("Result of test:\n",results)
    print("Permissions: \n",allowedUserPermission)
    user.generateReport(results,allowedUserPermission,users)

except Exception as e:
    print(e)
    driver.close()