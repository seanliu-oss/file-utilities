#!/usr/bin/python3
import sys
import hashlib
'''
checksum.py
  Calculate md5 and sha1 checksum of files in a list of files
  Main objective is to find the duplicates in the lists. So if both md5 and sha1 digests match it's more than likely the files are identical
  Arguments:
    A file containing a list of files
'''

def double_hash(filename):
    '''
    double_hash()
    Calculate md5 and sha1 of a file
    Parameters
        A file name
    Returns
        md5 and sha1 checksum of the file
    '''
    # Set BUF_SIZE  to 1MB so not to read whole file into memory
    BUF_SIZE = 1048576  # lets read stuff in 1MB chunks!

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return md5.hexdigest(), sha1.hexdigest()

def print_hashes(filename):
    '''
    print_hashes
    Prints md5 and sha1 checksum of a given file
    Parameters:
        The name of a file
    '''
    m,s=double_hash(filename)
    print("{} {} {}".format(m,s,filename))

def main(filelist):
    with open(filelist,"rt") as filelist:
         files=filelist.readlines()

    for f in files:
        print_hashes(f.strip())

if __name__ == "__main__":
    main(sys.argv[1])
