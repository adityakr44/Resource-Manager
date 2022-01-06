from res_manager import tmsl_records
from datetime import datetime

resource = {} # dictionary to store how many times a file was accessed and duration of access
              # dictionary key is a tuple: (dept,year)
              # dictionary value is a list: [times accessed, duration of access]

logs = open("G:\TMSL\logs.txt", "a") # opening the log file

# writing the current date and time to the log file

now = datetime.now() 
dt = now.strftime("%d/%m/%Y %H:%M:%S")
dt = "\n" + dt
logs.write(dt)
logs.write("\n")

# queries
# main() takes 3 arguments: departments, year, and choice 
# department = ["CE","CSE","ECE","EE","FT","IT","ME", "all"] 
# year = ["1","2","3","4","all"]
# choice = 1: Pass numbers, 2: Pass_categories

t = tmsl_records(resource)
resource = t.main("all", "all", 1)#query 1 : To get the pass numbers of all deparments all years.
print("\n")
resource = t.main("all", "all", 2)#query 2 : To get the pass categories of all deparments all years.
print("\n")
resource = t.main("IT", "all", 1)#query 3 : To get the pass numbers of IT deparment all years.
print("\n")
resource = t.main("IT", "2", 2)#query 4 : To get the pass categories of IT deparment 2nd year.
print("\n")
resource = t.main("CSE", "4", 1)#query 5 : To get the pass numbers of CSE deparment 4th years.
print("\n")
resource = t.main("ECE", "all", 2)#query 6 : To get the pass categories of ECE deparment all years.
print("\n")
resource = t.main("all", "1", 1)#query 7 : To get the pass numbers of all deparments 1st year.
print("\n")
resource = t.main("all", "3", 2)#query 8 : To get the pass categories of all deparments 3rd year.
print("\n")
resource = t.main("3", "ECE", 3)# test case to check if query is right
print("\n")

# updating the log file 

logs.write("Dept\tYear\tTimes Accessed\tDuration")
print("Dept\tYear\tTimes Accessed\tDuration")
for key,value in resource.items():
    line = "\n" + key[0] + "\t" + key[1] + "\t" + str(value[0]) + "\t\t" + str(value[1])
    print(line)
    logs.write(line)
logs.write("\n")

logs.close()
