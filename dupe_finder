import os

def dig(directory):
    c_path = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            c_path.append(path)
        else:
            dig(path)
    return c_path

def checksum(directory):
    list = dig(directory)
    for filename in list:
        cmd = "md5 " + filename
        fp = os.popen(cmd)
        value = fp.read()
        print value

