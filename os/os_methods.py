'''
Examples of using methods in os module
By Binggang Liu
'''

import os
from datetime import datetime
import glob

'''
# print out the current working directory
print(os.getcwd())

# print out the home directory
print(os.environ.get('HOME'))

# change the current working directory
os.chdir('/Users/binggangliu/Downloads')

# another way to change path (directory)
os.getcwd() # return current working directory: e.g. '/Users/binggangliu'
new_path = os.path.join(os.getcwd(),'./Downloads')
os.chdir(new_path) # will change the cwd to '/Users/binggangliu/Downloads'

# find files (e.g. excel xlsx files) in directory
os.chdir("/Users/binggangliu")
for file in glob.glob("*.xlsx"):
    print(file)

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
