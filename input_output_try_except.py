'''
Adding info to an existing document
By Binggang Liu

This program adds name and ID to an exixsting file and then write to a new file.
Exception handling is used for each section of the program: (1) taking input from command line; 
(2) reading file from local directory; (3) writing file to local directory

Note that input() returns a string though the number is entered is an integer.
int() can take an integer in string format and convert to an integer, but it cannot convert
a float in string format to an integer, though it can take a float and convert it to integer, e.g.:
  int('123.21') does not work, int(123.21) will return 123

One other point worth mentioning is the comparison of int() with round(), for example, int(3.7) gives 3, 
  while round(3.7) gives 4, int() returns integer type, whil round() returns float type.

'''

# Input Name and ID from command line:
while True:
    #  'True' means the condition for prompting the input at the command line. When a valid input entered,
    #    it will break the loop, so that the condition for prompting input at command line is no longer 'True'.
    try:
        input_name = input("Please enter the applicant's name: ")
        input_id = input("Please enter the applicant's ID: ")
        input_id_int = int(input_id)
        break
        # "break" statement will make program exit the loop, skip the steps below and go to "finally" directly,
        #  the 'break' statement will also skip the "else" statement even when the 'else' statement below become live.
    except ValueError as ve:
        print("This is not a valid ID, please try again to enter the ID as an integer")
        print(ve)
    except NameError as ce:
        print("Something is wrong with the code")
        print(ce)
        raise ce
    except:
        print("Something went wrong beyond ValueError and NameError")
        raise
    # else:
    #    print("Everything went alright!!")
    finally:
        print("a value has been entered")


# Read file from local directory:
try:
    with open('/Users/binggangliu/Downloads/DataEngineer.txt') as input_file:
        my_input_file = input_file.read()
        # print(my_input_file)
        #    print(input_file.read())
        '''
        for line in input_file:
            if line[0] == '*':
                print(line.strip())
        '''
except FileNotFoundError as rfe:
    print("Read file error")
    print(rfe)

# Write a new file to local directory with information added (Applicant's Name and ID)
try:
    with open('/Users/binggangliu/Downloads/MyModified.txt', 'w') as output_file:
        # if use option 'a' instead of 'w', the new file will append to the existing file each time running the program
        # for line in new_text:
        #    output_file.write(line + input_id)
        output_file.write(input_id + ' - ' + input_name +
                          '\n' + '\n' + my_input_file)
except NameError as wce:
    print("Write file error")
    print(wce)
