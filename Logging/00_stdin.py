import sys
 
# Standard input – This is the file-handle that a user program reads to get information from the user. We give input to the standard input (stdin).

# >>> sys.__stdin__
# <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>

stdin_fileno = sys.stdin
 
# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))