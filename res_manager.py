import os 
import time

class tmsl_records():
    def __init__(self, resource):
        # constructor to initialize the resource dictionary
        # dictionary key is a tuple: (dept,year)
        # dictionary value is a list: [times accessed, duration of access]
        
        self.resource = resource
        
    def add_res(self, dept, year):
        # function to generate the path to the file requested and read the data from it
        # also update the resource dictionary with times accessed and access duration
        
        data = None
        marks = None
        f = None
        t1 = time.time() # begin time of access
        
        if (dept,year) not in self.resource: # checking whether data is already present in dictionary
            self.resource[(dept,year)] = [1,0]
        
        else: # data is already present and update the times accessed
            self.resource[(dept,year)][0] += 1 
            
        path = os.path.join(os.path.sep, "G:\TMSL", dept, year, "StudentResult.txt") # generating path to the file requested
        f = open(path, "r")
        data = f.readlines() # reading the data in the file and storing in list
        marks = []
        for each in data: # finding the marks of each roll number and adding to a list 
            cols = each.split("\t")
            marks.append( [float(cols[2]), float(cols[3]), float(cols[4])] )
        
        t2 = time.time() # end time of access
        duration = t2 - t1 # duration of access 
        self.resource[(dept,year)][1] += duration # updating the duration of access
        f.close()
        return marks # returning marks of each student 
                
    def pass_numbers(self, dept, year):
        # function to find the number of students who passed in given dept and year
        
        marks = self.add_res(dept, year) # requesting marks of each student
        n = 0
        for each in marks: 
            avg = sum(each)/3.0
            if( avg >= 6.0 ):
                n += 1
        
        return n # returning number of students who passed
    
    def pass_categories(self, dept, year, categories):
        # function to find number of students in each grade point category
        
        marks = self.add_res(dept,year) # requesting marks of each student
        for each in marks:
            avg = sum(each)/3.0
            if( avg <= 10.0 and avg > 9.0 ):
                categories[1] += 1
            elif( avg <= 9.0 and avg > 8.0 ):
                categories[2] += 1
            elif( avg <= 8.0 and avg > 7.0 ):
                categories[3] += 1
            elif( avg <= 7.0 and avg > 6.0 ):
                categories[4] += 1
            else:
                categories[5] += 1
            
        return categories # returning updated categories
        
    def main(self, D, Y, ch):
        d = ["CE","CSE","ECE","EE","FT","IT","ME","all"] # list of valid departments
        y = ["1","2","3","4","all"] # list of valid years
        choices = [1,2] # list of valid choices
        
        if( D not in d or Y not in y or ch not in choices ): # checking whether queries are correct or not
            print("Query is Incorrect")
            return self.resource
        
        d.remove("all")
        y.remove("all")
        
        if( ch == 1 ): # if choice is 1: pass number of students
            n = 0
            if( D == "all" and Y == "all" ): # checking if all departments and years have to be checked
                for dept in d:
                    for year in y:
                        n += self.pass_numbers(dept, year)
                print("Pass Results for all departments and all year are: ")
            
            elif( D == "all" and Y != "all" ): # checking if all department and a particular year have to be checked
                for dept in d:
                    n += self.pass_numbers(dept, Y)
                print("Pass Results for all departments and year",Y,"are: ")
                
            elif( D != "all" and Y == "all" ): # checking if a particular department and all years have to be checked
                for year in y:
                    n += self.pass_numbers(D, year)
                print("Pass Results for",D,"department and all years are: ")
                
            else: # else a particular department and year have to be checked
                n += self.pass_numbers(D, Y)
                print("Pass Results for",D,"department and year",Y,"are: ")
                    
            print("Number of students that passed are: ", n)
        
        else: # if choice is 2: pass categories of students
            categories = {1:0, 2:0, 3:0, 4:0, 5:0} # dictionary to store number of students in each category
                                                   # 1: 10.0 to 9.0
                                                   # 2: 9.0 to 8.0
                                                   # 3: 8.0 to 7.0
                                                   # 4: 7.0 to 6.0
                                                   # 5: Less than 6.0
                                                   
            if( D == "all" and Y == "all" ): # checking if all departments and years have to be checked
                for dept in d:
                    for year in y:
                        categories = self.pass_categories(dept, year, categories)
                print("Pass Results for all departments and all year are: ")
            
            elif( D == "all" and Y != "all" ): # checking if all department and a particular year have to be checked
                for dept in d:
                    categories = self.pass_categories(dept, Y, categories)
                print("Pass Results for all departments and year",Y,"are: ")
                
            elif( D != "all" and Y == "all" ): # checking if a particular department and all years have to be checked
                for year in y:
                    categories = self.pass_categories(D, year, categories)
                print("Pass Results for",D,"department and all years are: ")
                    
            else:
                categories = self.pass_categories(D, Y, categories) # else a particular department and year have to be checked
                print("Pass Results for",D,"department and year",Y,"are: ")
                
            print("Grade Point\tNumber of Students")
            print("10.0 - 9.0 \t\t",categories[1])
            print("9.0 - 8.0  \t\t",categories[2])
            print("8.0 - 7.0  \t\t",categories[3])
            print("7.0 - 6.0  \t\t",categories[4])
            print("less than 6.0\t\t",categories[5])
        
        return self.resource