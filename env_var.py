import os
try:
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    PASSWORDS = os.getenv("PASSWORDS").split(",\n")
    USERS = os.getenv("USERS").split(",\n")
    #os.environ.get("USERS").split(",")
    #USERS="sysadmin@test.com,useradmin@test.com'".split(",")
    print(DB_HOST)
    print(DB_USER)
    print(DB_NAME)
    print(PASSWORDS)
    print(USERS)
except Exception as e:
    print(e)