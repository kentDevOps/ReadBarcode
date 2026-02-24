import os,sys

def chk_mandatory_folder(strFolder_name):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    strFolderPath = os.path.join(strDirPath,strFolder_name)
    if not os.path.isdir(strFolderPath):
        raise FileNotFoundError(f"Folder {strFolderPath} is not exists!!!")