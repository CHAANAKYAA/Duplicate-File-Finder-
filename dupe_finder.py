import os
import hashlib

def dig(directory):
    c_path = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            c_path.append(path)
        else:
            c_path += dig(path)
    return c_path

def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def checksum(directory):
    list = dig(directory)
    record = {}
    duplicates = {}
    for filename in list:
        value = md5(filename)
        if value in record:
            record[value]+=1
            print filename , record[value]
            duplicates[filename] = "c"
        else:
            record[value]=1
            print value , record[value]
    print duplicates
    return record
