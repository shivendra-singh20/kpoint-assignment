#! usr/bin/python2.7

"""
Write a test suite for verifying basic operations of Linux/Windows file system operation.
1. File write/read operations.
2. File Permissions.
"""

import os
import stat

home_path = os.getcwd()
dir_name = 'assignment'
if not os.path.exists(home_path + os.sep + dir_name):
    new_dir = os.mkdir(home_path + os.sep + dir_name)

os.chdir(dir_name)
f_path = os.getcwd() + os.sep + 'log.txt'

with open(f_path, 'w+') as fh:
    os.chmod(f_path, 436)
    print 'File mode changed successfully!!'
    fh.write('Hi, \nThis is Shivendra Singh, \nAnd I have done the assignment.\n')


with open(f_path, 'r') as fh:
    print fh.read()
