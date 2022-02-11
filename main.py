#Librarys
import random
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
url = 'http://localhost:3000/'
url = 'http://vectordev.vectorstat.com/'
url = 'http://vectorint.vectorstat.com/' 

def getName(email):
    name = email.split("@")
    print(name[0])
    return name[0]


usersList = []
results = []
userTestResult = [] #b
allowedUserPermissionsFromDB = [] #permisos permitidos para usuarios $allowedUserPermissionsFromDB
debug = False
try:
    try:
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")
        DB_USER = os.getenv("DB_USER")
        DB_PASS = os.getenv("DB_PASS")
        if debug != True:
            PASSWORDS = os.getenv("PASSWORDS").split(",\n")
            USERS = os.getenv("USERS").split(",\n")
            NAMES= os.getenv("NAMES").split(",\n")
            LASTNAMES = os.getenv("LASTNAMES").split(",\n")
            EMAILS = os.getenv("EMAILS").split(",\n")
        else:
            PASSWORDS = os.getenv("PASSWORDS").split(",")
            USERS = os.getenv("USERS").split(",")
            NAMES= os.getenv("NAMES").split(",")
            LASTNAMES = os.getenv("LASTNAMES").split(",")
            EMAILS = os.getenv("EMAILS").split(",")
        
    except Exception as e:
        print(e)

    print(DB_HOST)
    print(DB_NAME)
    print(DB_USER)
    print(DB_PASS)
    print(USERS)
    print(NAMES)
    print(LASTNAMES)
    print(EMAILS)

    driver.get(url)
    user = vectorStat()
    user.setConecction(driver,url)
    
    for i in range(len(USERS)):
        user.setSession(USERS[i],PASSWORDS[i])
        print(USERS[i])
        print(PASSWORDS[i],"\n")
        name = getName(user.getEmail())
        usersList.append(name)
        user.clearHistory()
        
        user.logIn()
        #UNIT
        added = user.addUnit()
        userTestResult.append(added)
        time.sleep(5)
        id = 'RD201024' #poner razon de porque está y ponerlo en archivo de constantes
        userTestResult.append(user.updateUnit(id))
        time.sleep(15)
        #Comprobar si es id get id unit  
        if added:
            userTestResult.append(user.deleteUnit(user.getIdUnit()))
        else:
            userTestResult.append(user.deleteUnit(id))
        time.sleep(10)

        #NOTES
        userTestResult.append(user.viewUnitNotes(id))
        time.sleep(10)      
        userTestResult.append(user.addUnitNote(id))
        time.sleep(10)

        #LOGO
        userTestResult.append(user.addLogo())
        time.sleep(5)
        userTestResult.append(user.viewLogo("Test logo"))
        time.sleep(5)
        #user.updateLogo("Nuvve - SDGE")        
        userTestResult.append(user.updateLogo("Test logo"))
        time.sleep(5)
        userTestResult.append(user.deleteLogo("Test logo"))
        time.sleep(5)
        
        #USER
        itemName = random.randint(0,6)
        itemLastname = random.randint(0,6)
        itemEmail = random.randint(0,6)
        userTestResult.append(user.addUser(NAMES[itemName],LASTNAMES[itemLastname],EMAILS[itemEmail]))
        time.sleep(10)
        
        userTestResult.append(user.viewUser())
        time.sleep(5)
        
        user.logOut()
        
        results.append(userTestResult)
        userTestResult = []
        
        historyTestOrder = user.getHistoryTestOrder()
        user.setDbConecction(DB_NAME,DB_USER,DB_PASS,DB_HOST)
        verifiedHistory = user.hasPermission(historyTestOrder)
        allowedUserPermissionsFromDB.append(verifiedHistory) #$allowedUserPermissionsFromDBFromDatabase
        
        
        print("History: \n{}".format(historyTestOrder))
        #print("Permissions user has: \n{}".format(verifiedHistory))
        
        user.clearPermissionListFromDB()
        break
        
    print("Users List ",usersList)
    print("Result for each user tested:\n",results)
    print("List of permissions for each user from DB: \n",allowedUserPermissionsFromDB)
    user.generateReport(results,allowedUserPermissionsFromDB,usersList)
    driver.close()

except Exception as e:
    print(e)
    driver.close()