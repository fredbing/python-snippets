'''
Examples of using methods in sys module
By Binggang Liu
'''

import sys

print(sys.platform)
print(sys.version)
print(sys.path)

sys.stderr.write('This is stderr. \n')
sys.stderr.flush()
sys.stdout.write('THis is stdout. \n')

print(sys.argv)
# It will print out the name of this file (as the first argument): 'sys_methods.py'
# any arguments that follow the filename at the commandline will be printed out after the first argument,
# e.g., when execucte at the commandline like this: python3 sys_methods.py word 23 "hello-world" 567
# the output will be: ['sys_methods.py', 'word', '23', 'hello-world', '567']

# print out each of the argument to be entered at the command line
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(arg)
else:
    print('No argumants provided')

# add up all integers to be entered at the command line
if len(sys.argv) > 1:
    total = sum(int(arg) for arg in sys.argv[1:] if arg.isdigit())
    print('Total is ', total)
else:
    print('No argumants provided')
