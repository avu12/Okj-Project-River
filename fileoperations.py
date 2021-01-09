def create_file(filename):
    f = open(filename,"w")
    f.close()

def add_data_to_file(river_name,river_size,filename):
   f = open(filename,"a")
   try:
       river_size = int(river_size)
   except ValueError as e:
       print(e)
       return -1

   f.write(river_name+";"+str(river_size)+"\n")
   f.close()
