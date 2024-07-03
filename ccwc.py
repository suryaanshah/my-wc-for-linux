def takefilepath():
    file_path=str(input("enter file path please: "))


def bytesinfile(): # show the bytes of a file
    takefilepath()
    try:
        with open(file_path, 'rb') as file:
            return len(file.read())
    except FileNotFoundError:
        print("Enter the correct path please :) ")
        return None

print("Namaste, this is my implimentation of the wc program in linux in a more user friendly way.")

function=input(""" What do you want to do? \n1. Find out number of bytes (type 'c') \n2. Find out number of lines (type 'l')\n3. Find out number of words (type 'w')\n""")
    

  # number of lines
def numoflines():
    takefilepath()
    try:
        with open(file_path, 'rb') as file:
            lcount=sum(1 for line in file)
            return lcount
            
    except FileNotFoundError:
        print("Enter the correct path please :) ")
        return None

# number of words
def numofwords():
    takefilepath()
    try:
        with open(file_path, 'rb') as file:
            wcount=len((file.read()).split())
            return wcountc
            
    except FileNotFoundError:
        print("Enter the correct path please :) ")
        return None







if function=='c':
    print(bytesinfile())
elif function == 'l':
    print(numoflines())
elif function == 'w':
    print(numofwords())

