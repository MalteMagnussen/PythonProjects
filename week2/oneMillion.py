import webget

# Download the file in case we do not have it already
url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_million_digits.txt'
webget.download(url)

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:100] + "...")
print(pi_string[100:200] + "...")
print(len(pi_string))
