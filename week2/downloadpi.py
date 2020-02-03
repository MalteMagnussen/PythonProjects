import webget  # webget.py must be created first and added to this folder.

# Download the file in case we do not have it already
url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_30_digits.txt'
webget.download(url)
