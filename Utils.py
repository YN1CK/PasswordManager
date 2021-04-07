import os
import random as ran


def get_pw_count(parent, password: str, dictionary: dict):
    matches = 0
    for key in dictionary:
        if password == key:
            return 100
        if parent.decrypt(password) == parent.decrypt(dictionary[key][1]):
            matches += 1
    return matches


def generate_password(length: int, pin: bool = False, ger=True):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"§$%&/()=?<>|,;.:-_#\'+*~\\´`€@^°'
    if ger:
        chars += 'äöüßÄÖÜ'
    if pin:
        chars = '0123456789'
    pw = ""
    for i in range(0, length):
        char = chars[ran.randint(0, len(chars)-1)]
        if ran.randint(0, 1) == 0:
            pw += char
        else:
            pw = char + pw
    return pw


def manual():
    os.system("start manual.html")
