import subprocess
import datetime
import time
import os

data_file_path = './data'

if __name__ == '__main__':
    print(os.path.exists(data_file_path))
    if os.path.exists(data_file_path) == False:
        os.mkdir(data_file_path)
    while True:
        subprocess.Popen(['python', 'main.py'])
        time.sleep(10 * 2)
        # subprocess.Popen(['wc', '-l', '<', 'data/' + (datetime.datetime.now() + datetime.timedelta(minutes=-2)).strftime('%Y-%m-%d') + '.tsv'])
        time.sleep(10 * 16)
