# my linux command dictionary

dict = {'alias': 'let you give your own name to a command or sequence of commands',
        'cal': 'see calendar of a month or a whole year', 'cat': 'concatenate', 'chmod': 'read, write and execute permision',
        'chown': 'change file owner', 'curl': 'retrieve from URL', 'df': 'show size,used space and available space',
        'diff': 'compare 2 text files and show difference', 'echo': 'print a string to terminal',
        'env': 'view all system variables', 'printenv': 'view all system variables', 'set': 'view all system variables',
        'exit': 'end execution or log out of remote SSH session', 'find': 'track down files',
        'finger': 'short dump of user info', 'free': 'summary of memory usage',
        'grep': 'searches for lines containing a search pattern', 'groups': 'tells which groups a user is in',
        'gzip': 'compresses files', 'head': 'gives the top lines', 'history': 'previously issued commands',
        'kill': 'terminate a process by providing the PID of the process', 'less': 'view files without opening an editor',
        'man': 'user manual for commands', 'mv': 'move files and directories', 'passwd': 'change the password for a user',
        'ping': 'verify network connection with an IP address', 'ps': 'lists running processes with their process ID or PID',
        'pwd': 'print the working directory', 'shutdown': 'shutdown or reboot system',
        'ssh': 'connect to remote linux computer and log into account', 'sudo': 'root or superuser permission',
        'tail': 'the bottom lines', 'tar': 'creates an archive file',
        'top': 'shows a real-time display of data relating to your Linux machine',
        'uname': 'obtains system info of the Linux computer', 'w': 'lists the currently logged in users',
        'whoami': 'find out who you are logged in as or who is logged into an unnamed Linux terminal'}

# print my linux command dictionary

for key, val in dict.items():
    print("My Linux Dictionary:  {} : {}".format(key, val))
