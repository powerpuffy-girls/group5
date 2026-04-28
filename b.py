FILENAME = "my_diary.py"

def create_file():
    try:
        file = open(FILENAME, "x") 
        file.close()
        print("Diary file created!\n")
    except FileExistsError:
        print("Diary file already exists.\n")

def write_entry():
    entry = input("Write your diary:\n")
    FILENAME = "my_diary.py"

def create_file():
    try:
        file = open(FILENAME, "x") 
        file.close()
        print("Diary file created!\n")
    except FileExistsError:
        print("Diary file already exists.\n")

def write_entry():
    entry = input("Write your diary:\n")