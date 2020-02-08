import argparse

parser = argparse.ArgumentParser(
    description='A program that downloads a URL and stores it locally')

# Positional arg
parser.add_argument('url', help='url of the file you wish to download')

# Optional Arg [- , --]
parser.add_argument('-d', '--destination', default='default_file.exe',
                    help='The name of the file to store the contents found at the url in')


args = parser.parse_args()

myUrl = args.url

print(args.url)

print(parser.parse_args())
