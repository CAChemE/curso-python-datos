'''The following code searches for NEF files that do not have
a JPG copy and deletes them. This is intended to be used after
a manual selection of the best JPGfiles that the photographer (you) has
selected

Author: F.J. Navarro
LICENSE: MIT

It only runs on Python 3.x (tested on Windows 7 only)

DO NOT USE THIS CODE WITHOUT A PROPER BACKUP of your precious files or photos
'''

import os
import fnmatch
import sys

# Seriously, DO NOT USE THIS CODE WITHOUT A PROPER BACKUP

print("Program started...")

cwd = os.getcwd()
path = cwd

JPGfiles = []

# Creates a list with JPG files names without extension nor PATH
for root, dirs, files in os.walk(path):
    for file in files:
        if fnmatch.fnmatch(file, '*.JPG'): 
            JPGfiles.append(os.path.splitext(file)[0])

# Checks
DNGfiles_path = []
for root, dirs, files in os.walk(path):
    for file in files:
        if fnmatch.fnmatch(file, '*.NEF'): 
            name_wo_extension = os.path.splitext(file)[0]
            if not(name_wo_extension in JPGfiles):
                DNGfiles_path.append(os.path.join(root, file))
				
import sys

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

# Lists all the files							 
for file in DNGfiles_path:
    print(file)

confirmation = query_yes_no("Would you like to remove the files listed above? \
 Once deleted there is not going back!")

if confirmation is True:
	for file in DNGfiles_path:
		os.remove(file)
	print("NEF files deleted :D")
else:
	print("Deletion cancelled")