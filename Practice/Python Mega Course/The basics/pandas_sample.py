import time, os

import pandas as pd

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pd.read_csv("files/temps_today.csv")
        print(data.mean()['st1'])
        print(data.mean())
    else:
        print('File does not exist')
    
    time.sleep(10)