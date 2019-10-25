# linux command dictionary
# Write to excel sheet and csv formats

import xlsxwriter
import pandas as pd
import csv

dict = {'alias': 'let you give your own name to a command or sequence of commands',
        'cal': 'display a calendar of a month or a whole year',
        'cat': 'concatenate',
        'chmod': 'change read, write and execute permision',
        'chown': 'change file owner',
        'curl': 'retrieve from URL',
        'date': 'print the current date time',
        'df': 'show size,used space and available space',
        'diff': 'compare two text files and show difference',
        'echo': 'print any given string to the terminal',
        'env': 'view all system variables',
        'printenv': 'view all system variables',
        'set': 'view all system variables',
        'exit': 'end execution or log out of remote SSH session',
        'find': 'track down files',
        'finger': 'short dump of user info',
        'free': 'summary of memory usage',
        'grep': 'searches for lines containing a search pattern',
        'groups': 'tells which groups a user is in',
        'gzip': 'compresses files',
        'head': 'gives the top lines',
        'history': 'previously issued commands',
        'id': 'print real user id and other details related to the account',
        'kill': 'terminate a process by providing the PID of the process',
        'less': 'view files without opening an editor',
        'man': 'user manual for commands',
        'mv': 'move or rename files and directories',
        'passwd': 'change the password for a user',
        'ping': 'verify network connection with an IP address',
        'ps': 'lists running processes with their process ID or PID',
        'pwd': 'print the working directory',
        'shutdown': 'shutdown or reboot system',
        'ssh': 'connect to remote linux computer and log into account',
        'sudo': 'root or superuser permission',
        'tail': 'the bottom lines',
        'tar': 'create and extract archive files',
        'top': 'shows a real-time display of data relating to your Linux machine',
        'tree': 'print the directory structure',
        'uname': 'obtains system info of the Linux computer',
        'w': 'lists the currently logged in users',
        'wc': 'short for word count, count newlines, words and bytes of a file',
        'whoami': 'find out who you are logged in as or who is logged into an unnamed Linux terminal'
        }

'''
# print my linux command dictionary at terminal
for key, val in dict.items():
    print("My Linux Dictionary:  {} : {}".format(key, val))
'''

# write to excel worksheet with xlsxwriter
excel_workbook = xlsxwriter.Workbook(
    '/Users/binggangliu/gitprojects/commands.xlsx')
excel_worksheet = excel_workbook.add_worksheet()

row = 1
col = 0

for key in dict.keys():
    row += 1
    excel_worksheet.write(row, col, key)

    for item in dict[key]:
        excel_worksheet.write(row, col+1, "".join(dict[key]))
excel_workbook.close()

'''
# write to excel worksheet with pandas
df = pd.DataFrame(data=dict, index=[0])
df = (df.T)
# print(df)
df.to_excel('/Users/binggangliu/gitprojects/commands_pd.xlsx')
'''

'''
# write to csv format
# To write csv format with csv module, it needs to run python2 (errors with python3)
with open('/Users/binggangliu/gitprojects/commands_linux.csv', 'wb') as output:
    writer = csv.writer(output)
    writer.writerows(dict.iteritems())
'''
