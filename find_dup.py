#!/usr/bin/python3
import sys
'''
find_dup.py
Find duplicate files
Arguments
    A file with checksums and file names
    Each line is formatted as:
    md5sum sha1sum filename
'''

def find_duplicate(filename):
    '''
    find_duplicate
    Find duplicate files
    Parameter:
        A file with checksums and file names
        Each line is formatted as:
        md5sum sha1sum filename
    '''
    chksumDict={}
    with open(filename,'rt') as chksum:
         chk=chksum.readlines()
    for rec in chk:
        md5,_,rest=rec.strip().partition(" ")
        sha1,_,path=rest.partition(" ")
        chksum2=md5+sha1
        if chksumDict.__contains__(chksum2):
            print("File already existing, files: {}  and {}".format(path,chksumDict[chksum2]))
        else:
            chksumDict[chksum2]=path

def main(file):
    find_duplicate(file)

if __name__=="__main__":
    main(sys.argv[1])
