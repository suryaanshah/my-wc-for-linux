def bytesinfile(): # show the bytes of a file
    file_path=str(input("enter the file path please: "))
    try:
        with open(file_path, 'rb') as file:
            print(len(file.read()))
    except FileNotFoundError:
        print("Enter the correct path please :) ")
        return None

print("Namaste, this is my implimentation of the wc program in linux in a more user friendly way.")

function=input(""" What do you want to do? \n1. Find out number of bytes (type 'c') """)
    
if function=='c':
    bytesinfile()

