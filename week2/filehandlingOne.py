
# With is like "try-with" from java. Otherwise we'd have to call close()
# The "path" is relative to the current position of the .py program that is executing the open()
with open('pi_30_digits.txt') as file_object:
    # Now we can work in here with the file: "file_object"
    # Read gives back the entire file as one string.
    contents = file_object.read()
    # use .rstrip() if you wanna remove the last blank line that .read() adds.
    print(contents)

# __________________________________
# or you can read line by line
with open('pi_30_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# __________________________________
# its like promises in javascript. If you wanna save the contents, store them in a variable
filename = 'pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# __________________________________
# Example where we work with the contents:
filename = 'pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    # pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# __________________________________
