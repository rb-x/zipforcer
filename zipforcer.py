import zipfile
from threading import Thread
import optparse
import sys


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return


def main():

    parser = optparse.OptionParser(
        f"usage {sys.argv[0]} -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) or (options.dname == None):
        print(parser.usage)

    print(options, args)
    zFile = zipfile.ZipFile(options.zname)
    passFile = open(options.dname)
    attempts = 0
    guess = None

    for line in passFile.readlines():
        password = line.strip('\n').encode('utf8')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        attempts += 1
        guess = extractFile(zFile, password)
        print(f"[-]({attempts}) Attempt : {password.decode('utf8')}")

        if guess:
            print(f"[+] Password found  : {password.decode('utf8')}!")
            exit(0)
    else:
        print(
            f'password not found with {options.dname} , total attempts : {attempts}')


if __name__ == "__main__":
    main()
