#Haoan Wang 81808540
#Daniel Lin 38828036(this is my partner)

from pathlib import Path
import shutil

# Define file_print function to print all files in the specified file lst.
def file_print(file_lst:list) -> None:
    for file in file_lst:
        print(file)


# Define file_D function to get a list of files from a directory path.
def file_D(file_lst:list,dir_path:str) -> list:
    for file in sorted(list(dir_path.iterdir())):
        if file.is_file():
            file_lst.append(file)
    return file_lst


# Define file_r function to sort the files and file folds in the right order in a diretory.
def file_r(dir_path) -> list:
    a = []
    b = []
    for file in list(dir_path.iterdir()):
        if file.is_file():
            a.append(file)
        elif file.is_dir():
            b.append(file)
    return sorted(a) + sorted(b)


# Define file_R function to get a list of files from the directory and subdirectories.
# With the file_r function, we can get the files in the right order.
def file_R(file_lst:list,filer:list) -> list:
    for file in filer:
        if file.is_file():
            file_lst.append(file)
        elif file.is_dir():
            file_R(file_lst,file_r(file))    
    return file_lst


# Define file_A function to select all the files in the file list as interesting files.
def file_A(file_lst:list) -> list:
    return file_lst


# Define file_N function to select files with specified name as interesting files.
def file_N(file_lst:list,file_name:str) -> list:
    file_pass = []
    for file in file_lst:
        if file_name == file.name:
            file_pass.append(file)
    return file_pass


# Define file_E function to select files with specified extension as interesting files.
def file_E(file_lst:list,file_ext:str) -> list:
    file_pass = []
    for file in file_lst:
        if file_ext == file.suffix:
            file_pass.append(file)
    return file_pass


# Define file_T function to select files containing specified text as interesting files.
def file_T(file_lst:list,text_search:str) -> list:
    file_pass = []
    for file in file_lst:
        try:
            file_text = open(file).readlines()
            for line in file_text:
                if text_search in line:
                    file_pass.append(file)
                    break
        except:
            continue
    return file_pass


# Define file_less function to select files with size less than specified threshold as interesting files.        
def file_less(file_lst:list,num_less:int) -> list:
    file_pass = []
    for file in file_lst:
        file_size = file.stat().st_size
        if file_size < num_less:
            file_pass.append(file)
    return file_pass


# Define file_more function to select files with size more than specified threshold as interesting files.  
def file_more(file_lst:list,num_more:int) -> list:
    file_pass = []
    for file in file_lst:
        file_size = file.stat().st_size
        if file_size > num_more:
            file_pass.append(file)
    return file_pass


# Define file_F function to print the first line of the files in the interesting file list.
def file_F(file_interest:list) -> None:
    for file in file_interest:
        try:
            file_lines = open(file).readlines()
            print(file_lines[0].rstrip())           
        except:
            print('NOT TEXT')


# Define file_Du function to duplicate the files in the interesting file list.
def file_Du(file_interest:list) -> None:
    for file in file_interest:
        shutil.copy2(file, str(file) + ".dup")


# Define file_T function to touch the files in the interesting file list.
def file_T(file_interest:list) -> None:
    for file in file_interest:
        file.touch()

    
# Define error function to repeat to read the input when error.
def error() -> list:
    print('ERROR')
    return input('').split(' ',1)


# The first step of the program, get the files under consideration
def step1(input_lst1:list) -> list:
    try:
        if input_lst1[0] == 'D':
            file_lst = []
            dir_path = Path(input_lst1[1])
            file_D(file_lst,dir_path)
            print(dir_path)
            return file_lst

        elif input_lst1[0] == 'R':
            file_lst = []
            dir_path = Path(input_lst1[1])
            filer = file_r(dir_path)
            file_R(file_lst,filer)
            return file_lst

        else:
            input_lstE = error()
            return step1(input_lstE)
    except:
        input_lstE = error()
        return step1(input_lstE)
        

    
    
# The second step of the program, get the interesting file list from files under consideration.
def step2(input_lst2:list,file_lst:list) -> list:
    try:
        if input_lst2[0] == 'A' and len(input_lst2) == 1:
            return file_A(file_lst)


        elif input_lst2[0] == 'N':
            file_name = input_lst2[1]
            return file_N(file_lst,file_name)

        elif input_lst2[0] == 'E':
            file_ext = '.' + input_lst2[1].split('.')[-1]
            return file_E(file_lst,file_ext)

        elif input_lst2[0] == 'T':
            text_search = input_lst2[1]
            return file_T(file_lst,text_search)
            
        elif input_lst2[0] == '<':
            num_less = int(input_lst2[1])
            return file_less(file_lst,num_less)

        elif input_lst2[0] == '>':
            num_more = int(input_lst2[1])
            return file_more(file_lst,num_more)
            
        else:
            input_lstE = error()
            return step2(input_lstE,file_lst)
            
    except:
        input_lstE = error()
        return step2(input_lstE,file_lst)


# The third step of the program, to take action on the interesting files.
def step3(input_lst3:list,file_interest:list) -> None:
    if input_lst3[0] == 'F' and len(input_lst3) == 1:
        file_F(file_interest)
    elif input_lst3[0] == 'D'and len(input_lst3) == 1:
        file_Du(file_interest)
    elif input_lst3[0] == 'T'and len(input_lst3) == 1:
        file_T(file_interest)
    else:
        input_lstE = error()
        return step3(input_lstE,file_interest)
        
            
        
    

# Get inputs and process three steps.
def digging_in_the_dirt() -> None:
    input_lst1 = input('').split(' ',1)
    file_lst = step1(input_lst1)
    file_print(file_lst)
    
    input_lst2 = input('').split(' ',1)
    file_interest = step2(input_lst2,file_lst)
    file_print(file_interest)

    input_lst3 = input('').split(' ',1)
    step3(input_lst3,file_interest)
    quit












    
if __name__ == '__main__':
    digging_in_the_dirt()
