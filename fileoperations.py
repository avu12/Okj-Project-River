#TODO
def create_file():
    filename = input("Give me a filename:")
    f = open(filename,"w")
    f.close()

#TODO
def add_data_to_file():
   filename = input("Give me a filename:")
   f = open(filename,"a")
   river_name = input("River name:")
   river_size = input("River size:")
   try:
       river_size = int(river_size)
   except ValueError as e:
       print(e)
       return -1

   f.write(river_name+";"+str(river_size)+"\n")
   f.close()