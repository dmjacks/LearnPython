# From the sys module, import the argument variable feature
from sys import argv

# declare two arguments
script, filename = argv

# set txt equal to the open function and pass it the argv filename
txt = open(filename)

#print user input
print "Here's your file %r: " % filename

#print contents of text
print txt.read()

#enter filename again
print "Type the filename again: "

#set file_again equal to raw input
file_again = raw_input("> ")

#set txt_again equal to the open funtion and pass it file_again
txt_again = open(file_again)

#print the contents of the file again
print txt_again.read()

#close first file
txt.close()

#close second file
txt_again.close()