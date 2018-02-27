import os
import zipfile

def zipdir(path, myzip):
    length = len(path)
    for root, dirs, files in os.walk(path):
        folder = root[length:] # path without "parent"
        for file in files:
            myzip.write(os.path.join(root, file), os.path.join(folder, file))

if __name__ == '__main__':
    myzip = zipfile.ZipFile('dist.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('dist/', myzip)
    myzip.close()