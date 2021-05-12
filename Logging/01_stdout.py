import sys

# Standard output – The user program writes normal information to this file-handle. The output is returned via the Standard output (stdout).

# >>> sys.__stdout__
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

stdout_fileno = sys.stdout
 
sample_input = ['Hi', 'Hello from AskPython', 'exit']
 
for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')