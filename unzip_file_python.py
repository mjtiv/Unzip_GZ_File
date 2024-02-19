#!/usr/bin/env python3

import gzip
import shutil

# Original Code Source
# https://stackoverflow.com/questions/31028815/how-to-unzip-gz-file-using-python


def unzip_gz_file(zipped_file_name):

    """

    Param zipped_file_name: Name of the file being parsed

    Return NONE:

    """

    # Modify the name for writing out (2-Steps)
    out_file_name = zipped_file_name.rstrip("gz")
    out_file_name = out_file_name.rstrip(".")

    # Open the file and Read as a Binary
    with gzip.open(zipped_file_name, 'rb') as f_in:
        # Write the file out as a Binary
        with open(out_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return ()


def main():

    print ("Starting Program")
    print ("")
    print ("")

    zipped_file_name = "Homo_sapiens.GRCh38.111.gtf.gz"

    # Unzip the file GZ file
    unzip_gz_file(zipped_file_name)

    print ("Done Running Program")


if __name__=="__main__": 
    main() 
