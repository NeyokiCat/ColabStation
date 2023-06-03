import csv
import os

data = []
database_path = os.path.join(os.path.dirname(__file__),'database')
database = os.listdir(database_path)

# print(database_path)
# print(database)

def loadCSV(filename,code=0):
    data = []
    path_to_data = os.path.join(database_path,filename)
    if code == 0:
        with open(path_to_data) as csvfile: 
            tag = next(csv.reader(csvfile)) # read the first line as tags
            for row in csv.reader(csvfile): # save csv into data
                data.append(row)
    return [filename,path_to_data,tag,data]

for file in database:
    data.append(loadCSV(file))
    
# print(data)

acc0 = data[0][3]
status = data[1][3]

# Structure of 'data'
# data[file][0:Filename, 1:PathToFile, 2:Tag (the first line of the file), 3:FileData]
#
# Structure of 'acc0' (file = data[0])
# acc0[account][0:uid, 1:usr, 2:pwd, 3:last_login]
#
# Structure of 'status' (file = data[1])
# status[0:uid, 1:status (admin,normal,guest,ban)]



def valid_login(usr,pwd): # Varify logins
    if if_exsist(usr):
        for i in acc0:
            if i[1] == usr and i[2] == pwd:
                return True
            

def if_exsist(usr): # Check if user already exsist
    for i in acc0:
        if i[1] == usr:
            return True
        

def create_user(usr,pwd): # Create a new account
    if if_exsist(usr):
        return "User name already exsist! Please choose another one"
    else:
        return "Success"

def log_user_in(usr): # Login user
    return True
