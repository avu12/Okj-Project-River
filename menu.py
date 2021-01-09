import getdata
import fileoperations
from pathlib import Path
def start_menu():
    print("Please tell me what kind of river activity want to do today: \n")
    print("Press 1, if you want to get a minimum river from a file.")
    print("Press 2, if you want to get a maximum river from a file.")
    print("Press 3, if you want to get a average river from a file.")
    print("Press 4, if you want to check a river existance in a file.")
    print("Press 5, if you want to print all data from a file.")
    print("Press 6, if you want to create a new file.")
    print("Press 7, if you want to add data to a file.")

    
    inp = input("Choosen number:")
    filename = input("Please give me the requested filename:\n")
    localpath =Path(__file__).with_name(filename)
    if inp == "1":
        getdata.min_river(localpath)
    elif inp == "2":
        getdata.max_river(localpath)
    elif inp == "3":
        getdata.avg_river(localpath)
    elif inp == "4":
        r = input("Please give me the river name:\n")
        getdata.river_exist(localpath,r)
    elif inp == "5":
        getdata.print_all_data(localpath)
    elif inp == "6":
        fileoperations.create_file(localpath)
    elif inp == "7":
        river_name = input("River name:\n")
        river_size = input("River size:\n")
        fileoperations.add_data_to_file(river_name,river_size,localpath)
    else:
        print("Please choose a valid option!")
        start_menu()


start_menu()