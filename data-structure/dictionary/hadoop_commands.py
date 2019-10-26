# hadoop commands dictionary
# Write to excel sheet and csv formats

import xlsxwriter
import pandas as pd
import csv

dict = {'bin/hadoop fs <args>': 'invoke FS shell',
        'hdfs dfs version': 'print the Hadoop version',

        'hdfs dfs -appendToFile <localsrc> ... <dst>': 'append src(s) from local to destination; reads input from stdin and appends to destination',
        'hdfs dfs -appendToFile localfile /user/hadoop/hadoopfile': '(example) append single src from local file system to the destination file system',
        'hdfs dfs -appendToFile localfile hdfs://nn.example.com/hadoop/hadoopfile': '(example) append single src from local to the destination file system',
        'hdfs dfs -appendToFile localfile1 localfile2 /user/hadoop/hadoopfile': '(example) append multiple srcs from local to the destination file system',
        'hdfs dfs -appendToFile - hdfs://nn.example.com/hadoop/hadoopfile': '(example) read the input from stdin',
        'hdfs dfs -cat URI [URI ...]': 'copy source paths to stdout',
        'hdfs dfs -cat hdfs://nn1.eml.com/file1 hdfs://nn2.eml.com/file2': '(example) copy source paths to stdout',
        'hdfs dfs -cat file:///file3 /user/hadoop/file4': '(example) copy source paths to stdout',
        'hdfs dfs -chgrp [-R] GROUP URI [URI ...]': 'owner or a super-user change group association of files',
        'hdfs dfs -chmod [-R] <MODE[,MODE]... | OCTALMODE> URI [URI ...]': 'owner or super-user changes the permissions of files',
        'hdfs dfs -chown [-R] [OWNER][:[GROUP]] URI [URI ]': 'owner or super-user changes the owner of files',
        'hdfs dfs -copyFromLocal /home/local /user/dest': '(example) similar to "put", but the source is restricted to local',
        'hdfs dfs -count [-q] <paths>': 'count the number of directories, files and bytes under the paths that match the specified file pattern',
        'hdfs dfs -count hdfs://nn1.eml.com/file1 hdfs://nn2.eml.com/file2': '(example) output with -count: DIR_COUNT, FILE_COUNT, CONTENT_SIZE FILE_NAME',
        'hdfs dfs -count -q hdfs://nn1.eml.com/file1': '(example) output with -count -q: QUOTA, REMAINING_QUATA, SPACE_QUOTA, REMAINING_SPACE_QUOTA, ...',
        'hdfs dfs -cp [-f] URI [URI ...] <dest>': 'copy files from source to destination, allows multiple sources where destination must be a directory',
        'hdfs dfs -cp -f /user/hadoop/file1 /user/hadoop/file2': '(example) [-f] option overwrites destination if it already exists',
        'hdfs dfs -cp /user/hdp/file1 /user/hdp/file2 /user/hadoop/dir': '(example) when multiple source files are copied, the destination must be a directory',
        'hdfs dfs -du [-s] [-h] URI [URI ...]': 'display sizes of files and directories in the given directory or the length of a file',
        'hdfs dfs -dus <args>': 'display a summary of file lengths. This is an alternate form of hdfs dfs -du -s',
        'hdfs dfs -expunge': 'empty the trash',
        'hdfs dfs -get [-ignorecrc] [-crc] <src> <localdst>': 'copy files to the local file system',
        'hdfs dfs -get /user/source /home/local/dest': '(example) copy file or directory in HDFS source to local file path as destination',
        'hdfs dfs -getfacl [-R] <path>': 'display the Access Control Lists (ACLs) of files and directories',
        'hdfs dfs -getmerge <src> <localdst> [addnl]': 'take a src directory and a destin file as input and concatenate files in src into the destination local file',
        'hdfs dfs -ls /user/dataf': '(example) display a list of the contents of a directory',
        'hdfs dfs -ls -R': 'behave like -ls, but recursively displays entries in all subdirectories',
        'hdfs dfs -lsr <args>': 'recursive version of ls. similar to Unix ls -R',
        'hdfs dfs -mkdir /user/datafile': '(example) create directories',
        'hdfs dfs -moveFromLocal <localsrc> <dst>': 'similar to put command, except that the source localsrc is deleted after it is copied',
        'hdfs dfs -moveToLocal [-crc] <src> <dst>': 'display a "Not implemented yet" message',
        'hdfs dfs -mv URI [URI ...] <dest>': 'move files to destination, can move multiple srcs where desti is a directory. Moving across file systems not permitted',
        'hdfs dfs -put <localsrc> ... <dst>': 'copy src(s) from local to destination file system; read input from stdin and writes to destination file system',
        'hdfs dfs -put /home/local /user/dest': '(example) copy file or directory from local to destination within the DFS',
        'hdfs dfs -put localfile hdfs://nn.example.com/hadoop/hadoopfile': '(example) copy file or directory from local to destination',
        'hdfs dfs -put - hdfs://nn.example.com/hadoop/hadoopfile': '(example) read the input from stdin',
        'hdfs dfs -rm [-skipTrash] URI [URI ...]': 'delete files specified as args, only deletes non empty directory and files',
        'hdfs dfs -rmr [-skipTrash] URI [URI ...]': 'recursive version of delete',
        'hdfs dfs -setfacl [-R] [-b|-k -m|-x <acl_spec> <path>]|[--set <acl_spec> <path>]': 'set Access Control Lists (ACLs) of files and directories',
        'hdfs dfs -setrep [-R] [-w] <numReplicas> <path>': 'change replication factor of a file',
        'hdfs dfs -tail [-f] URI': 'display last kilobyte of the file to stdout',
        'hdfs dfs -text <src>': 'take a source file and outputs the file in text format',
        'hdfs dfs -touchz URI [URI ...]': 'create a file of zero length'
        }

'''
# print my linux command dictionary at terminal
for key, val in dict.items():
    print("My Linux Dictionary:  {} : {}".format(key, val))
'''

# write to excel worksheet with xlsxwriter
excel_workbook = xlsxwriter.Workbook(
    '/Users/binggangliu/gitprojects/hadoop_commands.xlsx')
excel_worksheet = excel_workbook.add_worksheet()

row = 1
col = 0

cell_format_bold = excel_workbook.add_format({'bold': True, 'italic': False})

excel_worksheet.write('A1', 'Hadoop Shell Commands', cell_format_bold)
excel_worksheet.write('B1', 'Descriptions', cell_format_bold)

excel_worksheet.set_column('A:A', 60)
excel_worksheet.set_column('B:B', 90)

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
df.to_excel('/Users/binggangliu/gitprojects/hadoop_commands_pd.xlsx')
'''

'''
# write to csv format
# To write csv format with csv module, it needs to run python2 (errors with python3)
with open('/Users/binggangliu/gitprojects/hadoop_commands.csv', 'wb') as output:
    writer = csv.writer(output)
    writer.writerows(dict.iteritems())
'''
