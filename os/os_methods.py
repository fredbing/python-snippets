'''
Examples of using methods in os module
By Binggang Liu
'''

import os
from datetime import datetime

'''
# print out the current working directory
print(os.getcwd())

# print out the home directory
print(os.environ.get('HOME'))

# change the current working directory
os.chdir('/Users/binggangliu/Downloads')

# list the files in the current working directory
print(os.listdir())

# create sub-directory in the current directory
os.mkdir('mysubdir')
# create multi-level sub-directories in the current directory
os.mkdirs('mysubdir2/mysubsubdir2')

# delete directories
os.rmdir('mysubdir')
os.rmdirs('mysubdir2/mysubsubdir2')

# rename a file
os.rename('mytest.csv', 'mynew.csv')

# print out stat info for a file
print(os.stat('lookfor_csv.py'))
# Here is an example of using stat() to obtain useful info, such as last modified time of the file
mod_time = os.stat('lookfor_csv.py').st_mtime
print(datetime.fromtimestamp(mod_time))

'''
# use walk() method to find the directory/file tree

for dirpath, dirnames, filenames in os.walk('/Users/binggangliu/IdeaProjects'):
    print('Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
