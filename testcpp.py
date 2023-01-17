'''
testcpp.py file is a python file that's run C++ compiled executable file.
I've use here this python intrpreter to runs C++ program
let's compile the C++ file first, using command:-
        g++ -o [name of .exe compiled file] [.cpp file name]

For an example in my case:- 
        g++ -o test_code test_code.cpp

And then run the command to call name of the .exe compiled file for example- 'for_Cpp_py.exe'

◘•NOTE•◘
'Now it is compile every time, when you change any programs in the C++ file'
'''
import os  # import essential modules


# there is the function for compile C++ program file and generate's a .exe of the cpp file
# print's the output on the terminal
def compileCpp(Cpp_file):

        # fileName variable stores file name without .cpp extention, i.e. drop the part of .cpp only,
        # and except all part will store in fileName
        fileName = Cpp_file.split('.')[0]   
        exe = fileName+'.exe'  # add only .exe at the last place of fileName
        # try if fileName.exe is exists in the specific folder
        try: 
                os.remove(exe)   # remove the existing fileName.exe 
                os.system(f'g++ -o {fileName} {Cpp_file}')  # and make a new same name of file of full path of Cpp_file
                os.system(exe)   # and run the cpp file by calling compiled .exe of cpp file

        # when it's checking file is existing or not..
        # if it's fail or not found any file with name of 'exe' variable, 
        # note: FileNotFoundError will return by 'os.system()'
        except FileNotFoundError:
                os.system(f'g++ -o {fileName} {Cpp_file}')   # so compile first with same command like above..
                # then run this file. and print's the result on terminal
                os.system(exe)


def runCppEXE(filepath):
        fileName = filepath.split('.')[0]
        exe = fileName+'.exe'
        os.system(exe)


def findComments(fileLocation):
    containt = ''
    with open(fileLocation, 'r') as file:
        for line in file.readlines():
            if '//' in line: 
                containt += line.replace('\n', '')
            
    return containt

###################################### CALL THE PROGRAM ########################################

# compileCpp('A:/BIOINFORMAICS/C++_programs/test_code.cpp')
# runCppEXE('A:/BIOINFORMAICS/C++_programs/test_code.cpp')