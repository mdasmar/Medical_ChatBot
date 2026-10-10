import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

files=['src/__init__.py',
'src/helper.py',
'src/prompt.py',
'setup.py',
'app.py',
'testing/test.ipynb']

for filepath in files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating emplty file;{filepath}")
    else:
        logging.info(f"{filename} already exists")
