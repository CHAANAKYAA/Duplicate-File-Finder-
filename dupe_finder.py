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
    record = {}
    for filename in list:
        cmd = "md5 " + filename
        fp = os.popen(cmd)
        value = fp.read()
        if value in record:
            record[value]+=1
        else:
            record[value]=1
    return record

