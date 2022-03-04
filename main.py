import os
import re
import shutil

files = [f for f in os.listdir('.') if os.path.isfile(f)]

dList = []

while True:
    for f in files:
        print(f'files => {files}')
        if "." in f and f == "main.py": 
            continue 

        result = re.sub(r'^.*?\.', "", f)

        if result not in dList:
            try:
                os.mkdir(result)
                dList.append(result)
            except OSError: 
                print("could not make dir")
        else: 
            print('dir already made')
        
        print(f)
        shutil.move(f'./{f}', f'{result}')

    break
