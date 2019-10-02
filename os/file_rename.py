'''
Script for renaming files in a directory
By Binggang Liu
'''

import os

os.chdir('/Users/binggangliu/Music/Audio Music Apps/Databases/Tags_copy')

# split file name and file extension and print them out
for file in os.listdir():
    # split file name and file extension
    file_name, file_ext = os.path.splitext(file)
    # print out file name and file extension separately
    # print(file_name)
    # print(file_ext)

    # Now split the filename into fn_p1, fn_p2, fn_p3

    # fn_p1, fn_p2, fn_p3 = file_name.split('-') #this does not work

    fn_p = file_name.split('-')

    # print(i for i in range(len(fn_p))) #this does not work--<generator object <genexpr> at 0x10c7f5c00>

    # for fn_p1, fn_p2, fn_p3 in fn_p: #this does not work
    #    print(fn_p1, fn_p2, fn_p3)

#    print(fn_p)

    # fn_p1 = fn_p[0] #this works
    # fn_p2 = fn_p[1] #this does not work.
    # fn_p3 = fn_p[2] #this does not work
    # print(fn_p1)
    # print(fn_p2)

    # for index, value in zip(range(len(fn_p)), fn_p): #this works
    #    print(index, value)

    # for index, value in enumerate(fn_p): #this works
    #     print(index, value)

    for i in range(len(fn_p)):
        if i == 0:
            fn_p1 = fn_p[i].strip()[4:]
#            print(fn_p1)
        elif i == 1:
            fn_p2 = fn_p[i].strip()[6:]
#            print(fn_p2)
        else:
            fn_p3 = fn_p[i].strip()

#            print('{}-{}-{}{}'.format(fn_p1, fn_p2, fn_p3, file_ext))

            file_rename = '{}-{}{}'.format(fn_p1, fn_p2, file_ext)

            os.rename(file, file_rename)
            # file have been renamed in the directory now!
