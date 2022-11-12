'''
testcpp.py file is a python file that's run C++ compiled executable file.
I've use here this python intrpreter to runs C++ program
let's compile the C++ file first, using command:-
        g++ -o [name of .exe compiled file] [.cpp file name]

For an example in my case:- 
        g++ -o for_Cpp_py test_code.cpp

And then run the command to call name of the .exe compiled file for example- 'for_Cpp_py.exe'

◘•NOTICE•◘
'compile updation not available i.e. don't compile every time to apply changes on the C++ file.'
'''
import os  # import essential modules

fileName = 'test_code.exe'   # specify name of the C++ compiled file

PATH = ''  # denotes a empty path variable which is stores the exact path of fileName

# os.getcwd() is use for defining current working folder, [0] for returning only drive name like 'A:\'
for root, dir, files in os.walk(f'{os.getcwd()[0]}:/'):
    # searching each file from list of files
    for f in files:
        if f == fileName:  # if given C++ compiled file is matched with any file from list of files 
            PATH += os.path.join(root, f)   # then add it's to the PATH variable through .join() method

# converting all \ to / by the replace method
file = PATH.replace('\\', '/')

# "A:/BIOINFORMAICS/C++_programs/for_Cpp_py.exe"  file path
# os.system() method to run command on CMD, 'file' is our full path of our file ehich is use as command
os.system(file)