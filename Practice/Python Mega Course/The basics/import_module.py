import time, os

while True:
    if os.path.exists('files/vegetables.txt'):
        with open("files/vegetables.txt") as myfile:
            print(myfile.read())
    else:
        print('File does not exist')
    
    time.sleep(10)