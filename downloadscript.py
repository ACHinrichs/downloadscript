import urllib.request as urllib
import re
import os
import io
import sys
import subprocess
import argparse

REG_FINDSTRING  = b"<a href=\"\/Lehre\/SS17\/DSA\/Uebung\d+.pdf"
REG_SUBSTRING   = b"<a href=\"\/Lehre\/SS17\/DSA\/"
URL_MATERIALS   = r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/"
URL_LECTURENOTES= r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php"
OUT_DIR     = r"Uebungen/"

def fetchHTML(URL):
    response = urllib.urlopen(URL)
    html = response.read()

    return html;


def detectScripts(html):
    # The detected scripts
    s=re.findall(REG_FINDSTRING, html)
    return s;

def updatePDFs(s, ls):
    changed = False
    pdfunite = ""
    for i in range(0, len(s)):
        s[i] = re.sub(REG_SUBSTRING, b"", s[i]).decode('utf8')
        if not s[i] in ls:
            with urllib.urlopen(URL_MATERIALS + s[i]) as response:
                source = response.read()
            file = open(OUT_DIR + s[i], "wb")
            file.write(source)
            file.close()
            
            print("fetched: " + s[i])
            changed = True
    return changed;

def download():
    html = fetchHTML(URL_LECTURENOTES)
    scripts = detectScripts(html)

    # To check wether there are already any pdfs on the machine 
    #ls = subprocess.check_output('ls DS/', shell=True)
    ls = ""
    try:
        ls = os.listdir(OUT_DIR)
    except (Exception):
        print(OUT_DIR+" doesn't exist, now creating");
        os.mkdir(r"./"+OUT_DIR)      
    # To keep track and inform the user
    changed = updatePDFs(scripts, ls)
    if not changed:
        print("You were all up to date nothing happened.")


# stuff to run always here such as class/def
def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--findREG", help="Regular expression, to search for the link standard is "+str(REG_FINDSTRING,"utf8"),type=bytes, default=REG_FINDSTRING)
    parser.add_argument("-s","--subREG", help="Regular expression, which will be removed from the found Links, to get the Filename. Standard is "+str(REG_SUBSTRING,"utf8"), type=bytes, default=REG_SUBSTRING)
    parser.add_argument("-m","--materialsDIR", help="Folder (remote) in which the files are stored. Standard is "+URL_MATERIALS, type=str, default=URL_MATERIALS)
    parser.add_argument("-u","--url", help="URL where the informations of the PDFs are. Standard is "+URL_LECTURENOTES, type=str, default=URL_LECTURENOTES)
    parser.add_argument("-o","--out", help="Outputdirectory. Standard is "+OUT_DIR, type=str, default=OUT_DIR)
    args=parser.parse_args()
    REG_FINDSTR=args.findREG
    REG_SUBSTRING=args.subREG
    URL_MATERIALS=args.materialsDIR
    URL_LECTURENOTES=args.url
    out_dir=args.out
    download()
    
