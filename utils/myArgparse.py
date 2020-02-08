import argparse
from PythonProjects.utils import webget

parser = argparse.ArgumentParser(
    description='A program that downloads a URL and stores it locally')

# Positional arg
parser.add_argument('url', help='url of the file you wish to download')

# Optional Arg [- , --]
parser.add_argument('-d', '--destination',
                    help='The name of the file to store the contents found at the url in')


args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()

    myUrl = args.url

    if (args.destination):
        myDest = args.destination
    else:
        #import mimetypes
        import os
        from urllib.parse import urlparse
        # type, encoding = mimetypes.guess_type(myUrl)
        # myExt = type
        fileName = os.path.basename(urlparse(myUrl).path)
        myDest = fileName  # +myExt

    webget.download(myUrl, myDest)  # , #myDest)
