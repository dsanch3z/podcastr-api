import os
import zipfile

def zipdir(path, myzip):
    length = len(path)
    myzip.write('podcastr.py')
    for root, dirs, files in os.walk(path):
        folder = root[length:] # path without "parent"
        for file in files:
            myzip.write(os.path.join(root, file), os.path.join(folder, file))

if __name__ == '__main__':
    myzip = zipfile.ZipFile('podcastr.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('py3/lib/python3.5/site-packages/', myzip)
    myzip.close()