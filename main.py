import os

PATH = os.path.dirname(__file__)
PATH_to_Collection = os.path.join(os.path.dirname(__file__),"COllections")
PATH_to_Whisper = os.path.join(PATH_to_Collection,"Whisper")
PATH_to_ecoute = os.path.join(PATH_to_Collection,"ecoute")

def find_env(path):
    for root, dirs, files in os.walk(path):
        for i in dirs:
            for r, d, f in os.walk(os.path.join(root,i)):
                if 'python.exe' in f:
                    print(os.path.join(os.path.join(root,i),"python.exe"))
                    return True
    print("Can't find env")
    return False

find_env(PATH_to_ecoute)