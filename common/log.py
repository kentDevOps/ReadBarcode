import os
import sys
from datetime import datetime
import traceback
import configparser
def testLog():
    a= 5
    b= 0
    return a/b
    print(e)
def get_details_error(loi):
    tb =  traceback.extract_tb(loi.__traceback__)
    if tb:
        frame = tb[-1]
        file = frame.filename
        line = frame.lineno
        func = frame.name
        return file,func,line
    return None, None, None
def getRelativePath():
    #c = os.path.abspath(__file__)
    strAbsPath = os.path.abspath(sys.argv[0])
    strCurrPath = os.path.dirname(strAbsPath)
    strLogPath = os.path.join(strCurrPath,"log")
    if not os.path.exists(strLogPath):
        os.makedirs(strLogPath)
        return strLogPath
    else:
        return strLogPath
def logExport(ex):
    strLogPath = getRelativePath()
    strFilePath = strLogPath + r"\log_"  +  datetime.now().strftime("%Y%m%d") +".txt"
    strContents = "[{}] {}".format( datetime.now().strftime("%Y/%m/%d %H:%M:%S"),ex)
    if not os.path.exists(strFilePath):
        
        logFile = open(strFilePath,"x")
        logFile.writelines("\n")
        logFile.writelines(strContents)
        logFile.close()
    else:
        logFile = open(strFilePath,"a")
        logFile.writelines("\n")
        logFile.writelines(strContents)
        logFile.close()  
def read_ini(section,key):  
    config = configparser.ConfigParser()# Tạo một đối tượng ConfigParser để đọc file .ini
    strAbsPath = os.path.abspath(sys.argv[0])# Lấy đường dẫn tuyệt đối của file đang chạy (main.py)
    strCurrPath = os.path.dirname(strAbsPath)# Lấy thư mục chứa file đang chạy
    strLogPath = os.path.join(strCurrPath,"database","config.ini")# Tạo đường dẫn đến file config.ini trong thư mục database
    config.read(strLogPath,encoding='utf-8')# Đọc file config.ini
    rs = config[section][key]
    #port = config.getint('SERVER', 'Port')# Lấy giá trị của khóa 'Port' trong section 'SERVER' và chuyển nó thành số nguyên
    return rs
'''
# Ghi file config
config = configparser.ConfigParser()
config['SERVER'] = {'IP': '192.168.1.1', 'Port': '8080'}
with open('settings.ini', 'w') as configfile:
    config.write(configfile)
'''