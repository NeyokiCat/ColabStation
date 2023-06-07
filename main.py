import os

PATH = os.path.dirname(__file__)
PATH_to_Collection = os.path.join(os.path.dirname(__file__),"COllections")

def find_env(path):
    for root, dirs, files in os.walk(path):
        for i in dirs:
            for r, d, f in os.walk(os.path.join(root,i)):
                if 'python.exe' in f:
                    print(os.path.join(os.path.join(root,i),"python.exe"))
                    return True
    print("Can't find env")
    return False

def scan_for_env():
    for dir in os.listdir(PATH_to_Collection):
        if os.path.isdir(os.path.join(PATH_to_Collection, dir)):
            print(dir)
            find_env(os.path.join(PATH_to_Collection,dir))
            print("")
