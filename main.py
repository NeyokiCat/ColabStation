import os

PATH = os.path.dirname(__file__)
PATH_to_Collection = os.path.join(os.path.dirname(__file__),"COllections")
PATH_to_Whisper = os.path.join(PATH_to_Collection,"Whisper")
PATH_to_ecoute = os.path.join(PATH_to_Collection,"ecoute")

def find_env(path):
    for root, dirs, files in os.walk(path):
        if 'python.exe' in dirs:
            print(os.path.join(root,"python.exe"))
            return True
    print("Can't find env")
    return False

find_env(PATH_to_ecoute)