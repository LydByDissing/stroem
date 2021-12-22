#!/usr/local/bin/python3

import fitz
import sys, getopt
import os

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    doc = fitz.open(inputfile)
    page = doc.load_page(0)  # number of page
    pix = page.get_pixmap()
    pix.save(outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
