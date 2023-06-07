import os

PATH = os.path.dirname(__file__)
PATH_to_Collection = os.path.join(os.path.dirname(__file__),"COllections")

def find_env(path):
    for root, dirs, files in os.walk(path):
        if 'python.exe' in dirs:
            print(os.path.join(root,"python.exe"))
            return True
    print("Can't find env")
    return False

def scan_all_env():
    for dir in os.listdir(PATH_to_Collection):
        if os.path.isdir(os.path.join(PATH_to_Collection,dir)):
            print(dir)
            #find_env(dir)
        
scan_all_env()