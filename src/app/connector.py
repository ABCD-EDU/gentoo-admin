# File used to connect to database

import configparser
Config = configparser.ConfigParser()

Config.read("../../config.ini")
DB_USR = Config.get('DB', 'USR')
DB_PW = Config.get('DB', 'PW')
print(DB_USR, DB_PW)