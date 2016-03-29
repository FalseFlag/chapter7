import os

def run(**args):
    print "[*] in drlister module."
    files = os.lisdir(".")

    return str(files)
