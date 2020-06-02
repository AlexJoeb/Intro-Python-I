"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# -> open() takes two args. File name and read/write mode.
# -> Modes:
#   -> r - Read
#   -> r+ - Read/Write
#   -> w - Write
#   -> a - Appending (all text will be added to end of file.)

with open('foo.txt') as file:
    data = file.read()
    print(data)
    file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

create_bar_file = open('bar.txt', 'w')
create_bar_file.write('Voluptas laborum dignissimos consequuntur voluptas magnam.')
create_bar_file.close();

with open('bar.txt') as bar:
    data = bar.read()
    print(data);
    bar.close()

# YOUR CODE HERE