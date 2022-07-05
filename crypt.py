
from cryptography.fernet import Fernet

def encrypt(win, text: str, seed=None):
    if win.crypt:
        return text
    if seed is None:
        seed = win.conf[win.user]['SEED']
        f = Fernet(bytes(seed, encoding='utf-8'))
    else:
        f = Fernet(seed)
    return f.encrypt(bytes(text, encoding='utf-8')).decode('utf-8')

def decrypt(win, text: str, seed=None):
    if win.crypt:
        return text
    if seed is None:
        seed = win.conf[win.user]['SEED']
    f = Fernet(bytes(seed, encoding='utf-8'))
    temp = f.decrypt(bytes(text, encoding='utf-8')).decode('utf-8')
    return temp
