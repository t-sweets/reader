import time
import subprocess


def read():
    res = subprocess.check_output(['python2', 'pilibs/python2/nfc_reader.py'])
    print(res)
    return res.decode()
