# Start a new Python script by initializing a variable with a string
poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

# Create a file object and write content
file = open('poem.txt', 'w')

# add statements to write the string contained in the variable into the text file, then close that file
file.write(poem)
file.close()

# Then, add a statements to create a file object for the existing text file 'poem.txt' to read from
file = open('poem.txt', 'r')

# Now, add statements to display the contents of the text file, then close that file
for line in file:
    print(line, end='')
file.close()

# Now, add statements at the end of the program to append a citation to the text file then save the script file again
file = open('poem.txt', 'a')
file.write('(Oscar Wilde)')
file.close()

