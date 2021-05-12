import sys
 
# Save the current stdout so that we can revert sys.stdou after we complete
# our redirection
stdout_fileno = sys.stdout
 
sample_input = ['Hi', 'Hello from AskPython', 'exit']
 
# Redirect sys.stdout to the file
sys.stdout = open('Logging/logs/mysys_stdout.txt', 'w')
 
for ip in sample_input:

    # Prints to the redirected stdout (Output.txt)
    sys.stdout.write(ip + '\n')
    
    # Prints to the actual saved stdout handler
    stdout_fileno.write(ip + '\n')
 
# Close the file
sys.stdout.close()

# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno