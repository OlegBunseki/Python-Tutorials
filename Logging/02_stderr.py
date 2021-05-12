import sys

# Standard error – The user program writes error information to this file-handle. Errors are returned via the Standard error (stderr).
 
# >>> sys.__stderr__
# <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>

stdout_fileno = sys.stdout
stderr_fileno = sys.stderr
 
sample_input = ['Hi', 'Hello from AskPython', 'exit']
 
for ip in sample_input:
    # Prints to stdout
    stdout_fileno.write(ip + '\n')
    # Tries to add an Integer with string. Raises an exception
    try:
        ip = ip + 100
    # Catch all exceptions
    except:
        stderr_fileno.write('Exception Occurred!\n')