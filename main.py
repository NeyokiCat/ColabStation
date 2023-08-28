import os
import pynvml
import torch
import json

PATH = os.path.dirname(__file__)
PATH_to_Collection = os.path.join(os.path.dirname(__file__),"COllections")

class cmdline:
    import argparse
    parser = argparse.ArgumentParser(
                        prog='ColabStation',
                        description='A platform for collection of Ai tools',
                        epilog='')
    
    parser.add_argument("-s","--sourceS")
    
def scan_GPU():
    pynvml.nvmlInit()
    deviceCount = pynvml.nvmlDeviceGetCount()
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        print("GPU", i, ":", pynvml.nvmlDeviceGetName(handle), meminfo.total / (1024 ** 3))
    return i

def scan_GPU_total_mem():
    pynvml.nvmlInit()
    deviceCount = pynvml.nvmlDeviceGetCount()
    totalmem = 0
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        totalmem = totalmem + meminfo.total
    totalmem = totalmem / (1024 ** 3)
    return totalmem

def find_env(path): # Search python.exe under certain path
    for root, dirs, files in os.walk(path):
        for i in dirs:
            for r, d, f in os.walk(os.path.join(root,i)):
                if 'python.exe' in f:
                    print(os.path.join(os.path.join(root,i),"python.exe"))
                    return True
    print("Can't find env")
    return False

def scan_for_env(): # Search all python.exe location under Collections
    for dir in os.listdir(PATH_to_Collection):
        if os.path.isdir(os.path.join(PATH_to_Collection, dir)):
            print(dir)
            find_env(os.path.join(PATH_to_Collection,dir))
            print("")
            
class llm():
    def run_model(path_to_config,path_to_model,batch_size,device="GPU0"):
        torch.device(device)
        torch.compile(json.loads(path_to_config))
        
## Test area ##
# scan_for_env()
# scan_GPU()
# print(scan_GPU_total_mem())
