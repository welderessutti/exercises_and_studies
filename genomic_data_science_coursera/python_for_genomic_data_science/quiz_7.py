f = open("dataset/test.txt", "w")

f.write("testinggg...")

f.close()


def get_extension1(filename):
    return(filename.split(".")[-1])


def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])


def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]


print(get_extension3("myfile"))

mergefasta.py myfile1.fa myfile2.fa

import sys
tocheck = sys.argv[1]

import os

filenames = os.listdir("dataset")
f = open(filenames[0])
