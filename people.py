"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        # Return true if city change, successful, return false if city same as old city
        if new_city == self.city:
            return False
        else:
            self.city = new_city
            return True

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        assert len(self.branches) == 1 , "Employee has more than 1 branches to report to."
        if branchmap[self.branches[0]]["city"] == self.city:
            self.branches[0] = new_code
            return True
        else:
            return False

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position.
        assert position in ["Junior", "Senior", "Team Lead", "Director"] , "Position entered is not valid."
        self.position = position
    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary += (1.1*amt)
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        pos_dict = {"Director": 3 , "Team Lead": 2 , "Senior" : 1 , "Junior" : 0}

        if pos_dict[position] > pos_dict[self.position]:
            self.position = position
            self.increment(self.salary * 0.3)
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"[{self.name}, {self.age}, {self.ID}, {self.city}, {self.branches}, {self.position}, {self.salary}]"



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Rep", salary = None, superior = None): # Complete all this! Add arguments
        super.__init__(name, age, ID, city, branchcodes, salary)

        assert position in ["Rep", "Manager", "Head"] , "Position entered is not valid."
        self.position = position

        assert self.position == "Head" and superior is None, "Head should have no superior."
        self.superior = superior
    
    # def promote
    def promote(self, position:str) -> bool:
        pos_dict = {"Head": 2 , "Manager" : 1 , "Rep" : 0}

        if pos_dict[position] > pos_dict[self.position]:
            self.position = position
            self.increment(self.salary * 0.3)
            return True
        else:
            return False

    # def increment
    def increment(self, amt:int) -> None:
        self.salary += (1.05*amt)

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is None:
            return (None, None)
        else:
            for employee in sales_roster:
                if employee[2] == self.superior:
                    return (self.superior, employee[0])
            return (None, None)

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,

        #assert self.superior is None, "Superior ID already provided."
        
        if self.position == "Head":
            return False
        else:
            for employee in sales_roster:
                if self.position == "Rep":
                    if employee[5] == "Manager":
                        self.superior = employee[2]
                        return True
                else:
                    if employee[5] == "Head":
                        self.superior = employee[2]
                        return True
            return False


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(new_code)
        return True

    





    
    